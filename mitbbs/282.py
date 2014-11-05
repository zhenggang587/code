
base:两个指针从前向后找
优化：在第二个数组中二分查找
都没排序：用hash
如果一个数组很大，一个很小：对大的建hash，小的线性扫, assume m > n, nlog(m) < mlog(n)
分布在多台机器上：mapreduce，对A文件map输出(key, 'A')，对B输出(key, 'B')，reduce端count(distinct val) > 1则输出key
