import shutil
import tempfile

from ..transform import Transform


class TemporaryDirectory(Transform):
    """
    This transform returns a temporary directory that is removed on cleanup.
    """
    def _repr_model_(self):
        return self.__class__.__name__

    def transform(self):
        import girder_worker.utils

        self.temp_dir_path = tempfile.mkdtemp(dir=girder_worker.utils.get_tmp_root())
        return self.temp_dir_path

    def cleanup(self):
        shutil.rmtree(self.temp_dir_path, ignore_errors=True)
