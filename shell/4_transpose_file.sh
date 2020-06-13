# 题目： 给定一个文件 file.txt，转置它的内容。
# 你可以假设每行列数相同，并且每个字段由 ' ' 分隔.
# 
# 示例:
# 假设 file.txt 文件内容如下：
# name age
# alice 21
# ryan 30
# 
# 应当输出：
# name alice ryan
# age 21 30

# awk 方法 print 输出是有换行的； printf 输出没有换行
awk '
  {for (i=1; i<=NF; i++) {
    if (NR == 1) {
      res[i] = $i
    } else {
      res[i] = res[i]" "$i
    }
  }}
  END{for (j=1; j<=NF; j++) {
   printf res[j]
  }}' file.txt


# cut 方法 -d表示分割符号 -f表示输出字段位置 1表示第一列 一般 -d/-f 一起使用
fieldsNum=$(head -n1 file.txt | wc -w)

for i in $(seq ${fieldsNum}); do
  echo $(cut -d " " -f ${i} file.txt)
done
