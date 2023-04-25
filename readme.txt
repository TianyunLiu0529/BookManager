token: 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

Superuser: liu
	 : zmwxf0418

1.创建子应用，然后在setting里注册子应用
2.写子应用的结构（model）
3.迁移数据
	python manage.py makemigration 生成迁移文件 将类转换成表结构
	python manage.py migrate 执行迁移文件 这个时候数据库里才有这个表