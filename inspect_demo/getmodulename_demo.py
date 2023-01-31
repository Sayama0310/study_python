import inspect

# 実際に存在するPythonモジュールまでのパス
path = r'/Users/sayama_yusei/Documents/private/study_python/inspect_demo/getmodulename_demo.py'
print(inspect.getmodulename(path=path))  # getmodulename_demo


# 実際には存在しないが、Pythonモジュールとしては妥当な名前を持つパス (拡張子が.py)
path = r'/Users/sayama_yusei/Documents/private/study_python/inspect_demo/does_not_exist.py'
print(inspect.getmodulename(path=path))  # does_not_exist


# 実際には存在しないが、Pythonモジュールとしては妥当な名前を持つパス (拡張子が.so)
path = r'/Users/sayama_yusei/Documents/private/study_python/inspect_demo/special_extension.so'
print(inspect.getmodulename(path=path))  # special_extension


# Pythonモジュールとしては妥当でない名前を持つパス (拡張子が.md)
path = r'/Users/sayama_yusei/Documents/private/study_python/README.md'
print(inspect.getmodulename(path=path))  # None


# Pythonパッケージまでのパス
path = r'/Users/sayama_yusei/Documents/private/study_python/inspect_demo'
print(inspect.getmodulename(path=path))  # None
