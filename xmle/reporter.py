
import os
from .elem import Elem

class Reporter(Elem):

	def __init__(self, title=None):
		if title is None:
			super().__init__('div', {'class': 'larch_html_report'}, html_repr=-2)
			self.__seen_html_repr = 0
		else:
			super().__init__('div', {'class': 'larch_html_report'}, html_repr=-2)
			self.put('div', {'class':'larch_title'}, text=title)
			self.__seen_html_repr = len(self)

	def _repr_html_(self):
		result = "".join(_._repr_html_() for _ in self[self.__seen_html_repr:])
		self.__seen_html_repr = len(self)
		return result

	def __ilshift__(self, other):
		self << other
		self.__seen_html_repr = len(self)
		return self

	def section(self, title, short_title=None):
		s = self.__class__()
		if short_title:
			s << f"# {title} | {short_title}"
		else:
			s << f"# {title}"
		self << s
		return s

	def renumber_numbered_items(self):
		# Find all larch_caption classes
		caption_classes = set()
		for n, i in enumerate(self.findall(".//span[@larch_caption]")):
			caption_classes.add(i.attrib['larch_caption'])
		for caption_class in caption_classes:
			for n, i in enumerate(self.findall(f".//span[@larch_caption='{caption_class}']")): # 			for n, i in enumerate(self.findall(f".//span[@class='larch_{caption_class.lower().replace(' ','_')}_caption']")):
				i.text = re.sub(f"{caption_class}(\s?[0-9]*):", f"{caption_class} {n+1}:", i.text, count=0, flags=0)

	def save(self, *args, **kwargs):
		self.renumber_numbered_items()
		super().save(*args, **kwargs)

	def save_simple(self, filename, overwrite=True):
		if isinstance(overwrite, str) and overwrite[:8] == 'archive:':
			filedirname, filebasename = os.path.split(filename)

			if os.path.isabs(overwrite[8:]):
				# archive path is absolute
				archive_path = overwrite[8:]
			else:
				# archive path is relative
				archive_path = os.path.normpath(os.path.join(filedirname, overwrite[8:]))
			os.makedirs(archive_path, exist_ok=True)
			if os.path.exists(filename):
				# send existing file to archive
				from .file_util import next_filename, creation_date, append_date_to_filename
				import shutil
				epoch = creation_date(filename)
				new_name = next_filename(
					append_date_to_filename( os.path.join(archive_path, filebasename), epoch),
					allow_natural=True
				)
				shutil.move(filename, new_name)
			overwrite = False
		if os.path.exists(filename) and not overwrite:
			raise FileExistsError("file {0} already exists".format(filename))
		with open(filename, 'wt') as f:
			f.write( "".join( _1._repr_html_()  for _1 in list(self) ) )
		return filename
