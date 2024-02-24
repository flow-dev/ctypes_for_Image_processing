# ctypes_for_Image_processing

#### 基本はpythonで組んで,画像処理アルゴリズムだけC++で書きたい用のサンプルコード

#### Point

* ctypesを使う
* Windows/LinuxでC++ファイルの作り方,呼び方が異なる.
* numpy配列をポインタ型にしてC++関数に渡せるが,numpyの型指定必須.
* .cppの関数は,"extern "C" __declspec(dllexport)"つけないとpythonから外部参照できない
* Image_processing.pyから実行

#### DLLの作り方Tips

* Windows OS
  * Download <https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/rubenvb/gcc-4.8-release/>
  * "x86_64-w64-mingw32-gcc-4.8.0-win64_rubenvb.7z"
  * Build Dll for Windows 64bit System.
  * Reference <https://kakurasan.blogspot.jp/2015/07/debianubuntu-mingw-crosscompile.html>
  * Command
    * >>> x86_64-w64-mingw32-g++ -c Image_processing.cpp
    * >>> x86_64-w64-mingw32-g++ -shared -o Image_processing.dll Image_processing.o

* Linux OS
  * Build .so for linux System.
  * Command
    * >>> g++ -g -Wall -fPIC -o Image_processing.o -c Image_processing.cpp
    * >>> g++ -shared Image_processing.o -o Image_processing.so

#### 実行結果
python .\Image_processing.py
(array([10, 20, 30], dtype=uint8), array([40, 50, 60], dtype=uint8), array([10, 20, 30, 40, 50, 60, 70, 80, 90], dtype=uint8), array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=uint8))
(<__main__.LP_c_ubyte object at 0x000000000210FBC8>, <__main__.LP_c_ubyte object at 0x0000000002A12A48>, <__main__.LP_c_ubyte object at 0x0000000002AB0AC8>, <__main__.LP_c_ubyte object at 0x0000000002B548C8>)
210
[11 21 31 41 51 61 71 81 91]

