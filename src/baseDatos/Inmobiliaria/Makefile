.PHONY: clean inmobiliaria.sql drop populate

all: inmobiliaria.sql

inmobiliaria.sql:
	# SETUP
	touch inmobiliaria.sql
	cat setup.sql >> inmobiliaria.sql

	# CREACION DE TABLAS
	cat property.ddl >> inmobiliaria.sql
	cat seller.ddl >> inmobiliaria.sql
	cat property_type.ddl >> inmobiliaria.sql
	cat region.ddl >> inmobiliaria.sql

 	# INSERTAR VALORES
	cat property.dml >> inmobiliaria.sql
	cat seller.dml >> inmobiliaria.sql
	cat property_type.dml >> inmobiliaria.sql
	cat region.dml >> inmobiliaria.sql

	# METODOS
	cat property.sql >> inmobiliaria.sql
	cat seller.sql >> inmobiliaria.sql
	cat property_type.sql >> inmobiliaria.sql
	cat region.sql >> inmobiliaria.sql

deploy:
	psql postgres < inmobiliaria.sql

populate:
	psql inmobiliaria < sample_data.sql

drop:
	psql -c "DROP DATABASE IF EXISTS inmobiliaria;" postgres

clean:
	$(RM) inmobiliaria.sql
