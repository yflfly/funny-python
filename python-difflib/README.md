# difflib

可针对两个文档进行比较，并将比较的结果以HTML的结果显示<br>
difflib模块提供的类和方法用来进行序列的差异化比较，它能够比对文件并生成差异结果文本或者html格式的差异化比较网页，如果需要比较目录的不同，可以使用filecmp模块<br>

class difflib.SequenceMatcher <br>
此类提供了比较任意可哈希类型序列对方法。此方法将寻找没有包含‘垃圾'元素的最大连续匹配序列。<br>
通过对算法的复杂度比较，它由于原始的完形匹配算法，在最坏情况下有n的平方次运算，在最好情况下，具有线性的效率。<br>
它具有自动垃圾启发式，可以将重复超过片段1%或者重复200次的字符作为垃圾来处理。可以通过将autojunk设置为false关闭该功能。<br>

class difflib.Differ <br>
此类比较的是文本行的差异并且产生适合人类阅读的差异结果或者增量结果 <br>

参考网址:<br>
https://docs.python.org/zh-cn/3.7/library/difflib.html <br>