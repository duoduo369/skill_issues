Spark
===
很多代码来自 [Spark权威指南](https://github.com/databricks/Spark-The-Definitive-Guide)

pyspark使用ipython3
---

		export PYSPARK_DRIVER_PYTHON=ipython3


explain 查看执行命令，类似mysql
---

		In [1]: df = spark.range(10).toDF("N")

		In [2]: df.explain()
		== Physical Plan ==
		*(1) Project [id#0L AS N#2L]
		+- *(1) Range (0, 10, step=1, splits=8)

取某列的最大值
---

		from pyspark.sql.functions import max

		flightData2015.select(max("count")).take(1)


group by 并求和
---


    maxSql = spark.sql("""
    SELECT DEST_COUNTRY_NAME, sum(count) as destination_total
    FROM flight_data_2015
    GROUP BY DEST_COUNTRY_NAME
    ORDER BY sum(count) DESC
    LIMIT 5
    """)

    maxSql.show()


		from pyspark.sql.functions import desc

		flightData2015\
			.groupBy("DEST_COUNTRY_NAME")\
			.sum("count")\
			.withColumnRenamed("sum(count)", "destination_total")\
			.sort(desc("destination_total"))\
			.limit(5)\
			.show()
