-- ---------------------------------------------------------------------
-- ---------------------------------------------------------------------

--INSERT INTO rol
--	(nombre)
--VALUES
--	('System Admin'),
-- 	('Admin'),
-- 	('Usuario');

--INSERT INTO usuario 
--	(nombres, apellidos, correo, usuario, clave, is_active, id_rol) 
--VALUES 
-- 	('FRANCISCO', 'CARMONA', 'flcarmonac@yahoo.com', 'NEFELIN', HASHBYTES('SHA2_256', '123456'), 1, 1);

--INSERT INTO negocio
-- 	(nombre, rut, direccion, descripcion, logo, is_active)
--VALUES
-- 	('Kartax', '00.000.000-0', 'Vi�a del Mar', 'Demo', '/img/kartax/logo.ico', 1);

--INSERT INTO usuario_negocio 
-- 	(id_usuario, id_negocio, fecha)
--VALUES
-- 	(1, 1, GETDATE());

--INSERT INTO color (nombre, r, g, b, id_negocio) 
--VALUES 
-- 	('colorBase01', 0, 0, 0, 1),
-- 	('colorBase02', 255, 255, 255, 1),
-- 	('colorBase03', 102, 102, 102, 1),
-- 	('color01', 32, 148, 243, 1),
-- 	('color02', 190, 0, 29, 1),
-- 	('color03', 252, 161, 32, 1),
-- 	('color04', 0, 255, 255, 1);

--INSERT INTO tipo_alimento (nombre, img, is_active, id_negocio)
--VALUES 
-- 	('Para Beber', '/img/kartax/grupo_01.jpg', 1, 1),
-- 	('Tablas', '/img/kartax/grupo_03.jpg', 1, 1),
-- 	('Para chanchear', '/img/kartax/grupo_02.jpg', 1, 1);

--INSERT INTO item_categ (nombre, id_tipo_alimento) 
--VALUES 
-- 	('Cervezas Artesanales', 1),
-- 	('Cervezas Envasadas', 1),
-- 	('De la Casa', 2),
-- 	('Hamburguesas', 3),
-- 	('Completos', 3);

--INSERT INTO item (nombre, descripcion, precio, img, is_active, id_item_categ) 
--VALUES 
-- 	('Pils', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 5500, '/img/kartax/item_01.png', 1, 1),
-- 	('Santa Sed', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 4800, '/img/kartax/item_02.png', 1, 1),
-- 	('Blood', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 4500, '/img/kartax/item_03.png', 1, 1),
-- 	('Heineken', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 2500, '/img/kartax/item_04.jpg', 1, 2),
-- 	('Kross', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 3500, '/img/kartax/item_05.jpg', 1, 2),
-- 	('Kunstmann', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 2500, '/img/kartax/item_06.jpg', 1, 2),
-- 	('Budweiser', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 2000, '/img/kartax/item_07.jpg', 1, 2),
-- 	('Royal', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 2500, '/img/kartax/item_08.jpg', 1, 2),
-- 	('Tabla de Carne', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 7000, '/img/kartax/item_09.png', 1, 3),
-- 	('Tabla de Queso', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 7000, '/img/kartax/item_10.png', 1, 3),
-- 	('Tabla Veggie', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 7000, '/img/kartax/item_11.png', 1, 3),
-- 	('Papas R�sticas', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 5000, '/img/kartax/item_12.png', 1, 3),
-- 	('Papas Merken', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 5000, '/img/kartax/item_13.png', 1, 3),
-- 	('Papas Cheddar', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 6000, '/img/kartax/item_14.png', 1, 3),
-- 	('Hamburguesa de Res', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 6000, '/img/kartax/item_15.png', 1, 4),
-- 	('Hamburguesa Pollo Apanado', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 6000, '/img/kartax/item_16.png', 1, 4),
-- 	('Hamburguesa Doble Cheddar', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 6000, '/img/kartax/item_17.png', 1, 4),
-- 	('Hamburguesa Mechada', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 6000, '/img/kartax/item_18.png', 1, 4),
-- 	('Hamburguesa Veggie', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 6000, '/img/kartax/item_19.png', 1, 4),
-- 	('Hamburguesa Veggie Legumbres', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 6000, '/img/kartax/item_20.png', 1, 4),
-- 	('Completo Mexicano', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 3000, '/img/kartax/item_21.png', 1, 5),
-- 	('Completo Tocino', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 3000, '/img/kartax/item_22.png', 1, 5),
-- 	('Completo Italiano', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 3000, '/img/kartax/item_23.png', 1, 5),
-- 	('Completo Aleman', 'nace de lupulo y cebada, y vive en una botella encerrada, puede ser morena o dorada, puede ser de trigo o cereza, para ser sincero sin rodeo digo, buena amiga es la cerveza"', 3000, '/img/kartax/item_24.png', 1, 5);

--INSERT INTO rrss
--	(nombre, img)
--VALUES
-- 	('Facebook', '/img/RRSS/facebook2.svg'),
-- 	('Instagram', '/img/RRSS/instagram1.svg'),
-- 	('twitter', '/img/RRSS/twitter2.svg'),
-- 	('Whatsapp', '/img/RRSS/whatsapp1.svg');

--INSERT INTO mesa
-- 	(nombre, descripcion, is_active, id_negocio)
--VALUES
-- 	('Barra', 'Interna', 1, 1);

--INSERT INTO caja
-- 	(monto, fecha_ini, fecha_fin, id_usuario, is_active, is_pedido_active)
--VALUES
-- 	(500000, GETDATE(), NULL, 1, 1, 1);

-- ---------------------------------------------------------------------
-- ---------------------------------------------------------------------
SELECT * FROM rol;
SELECT * FROM usuario;
SELECT * FROM negocio;
SELECT * FROM usuario_negocio;
SELECT * FROM color;
SELECT * FROM item_grp;
SELECT * FROM item_categ;
SELECT * FROM item;
SELECT * FROM rrss;
SELECT * FROM mesa;
SELECT * FROM comanda;
SELECT * FROM comanda_deta;
SELECT * FROM caja;
------
SELECT * FROM rrss_negocio;
SELECT * FROM salida;
SELECT * FROM salida_deta;
------
SELECT * FROM pedidos 
SELECT * FROM pedidos_estado
SELECT * FROM encuesta

-- ---------------------------------------------------------------------
-- ---------------------------------------------------------------------
--DROP TABLE rol; 
--DROP TABLE usuario; 
--DROP TABLE negocio; 
--DROP TABLE usuario_negocio; 
--DROP TABLE color; 
--DROP TABLE tipo_alimento; 
--DROP TABLE item_categ; 
--DROP TABLE item; 
--DROP TABLE rrss;
--DROP TABLE mesa; 
--DROP TABLE comanda; 
--DROP TABLE comanda_deta; 
--DROP TABLE caja; 
--DROP TABLE rrss_negocio;
--DROP TABLE salida; 
--DROP TABLE salida_deta; 
------
--DROP TABLE pedidos; 
--DROP TABLE pedidos_estado; 
--DROP TABLE encuesta; 

-- ---------------------------------------------------------------------
-- ---------------------------------------------------------------------
--SELECT DATEADD(MINUTE, 60, token_fecha), * FROM usuario 

-- SP Public ---------------------------------
EXECUTE pa_usuario_logearse 'NEFELIN', 'SECRET-KEY'
--EXECUTE pa_usuario_registrarse 'FRANCISCO', 'CARMONA', 'flcarmonac@yahoo.com', 'NEFELIN', 'SECRET-KEY'
EXECUTE pa_usuario_validar 'NEFELIN', 'SECRET-TOKEN'

EXECUTE pa_negocio_get
EXECUTE pa_negocio_get_byid 1
EXECUTE pa_negocio_get_byid_usuario 1

EXECUTE pa_item_grp_get_byid 1
EXECUTE pa_item_grp_get_byid_negocio 1

EXECUTE pa_item_categ_get_byid 1
EXECUTE pa_item_categ_get_byid_grp 1
EXECUTE pa_item_categ_get_byid_negocio 1

EXECUTE pa_item_get_byid 1
EXECUTE pa_item_get_byid_categ 1
EXECUTE pa_item_get_byid_negocio 1

-- SP Private --------------------------------
DECLARE @id AS INT
SET @id = (SELECT id_usuario FROM kartax_usuario WHERE (correo = 'NEFELIN' OR usuario = 'NEFELIN') AND sql_token = 'SECRET-TOKEN')
SELECT ISNULL(@id, 0)



