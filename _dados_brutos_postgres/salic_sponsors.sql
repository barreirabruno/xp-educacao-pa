CREATE TABLE IF NOT EXISTS sponsor_salic (
	id SERIAL PRIMARY key,
	id_sponsor_salic character varying(60) NOT null,
	sponsor_name character varying(255) NOT null,
	cgccpf character varying(22) NOT null,
	tipo_pessoa character varying(25) NOT null,
	responsavel character varying(100) NOT null,
	total_doado character varying(25) NOT null,
	uf character varying(2) NOT null,
	municipio character varying(30) NOT null,
	created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  	updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

INSERT INTO public.sponsor_salic (id_sponsor_salic,sponsor_name,cgccpf,tipo_pessoa,responsavel,total_doado,uf,municipio,created_at,updated_at) VALUES
	 ('5afec5523308eb0d860f5f568c31bedd7268cb38ea27d861b6327cbdd8ef','Galvani Industria Comércio e Serviço Ltda.','00546997000180','juridica','José Rubens Blasi Carvalho Rosas','2905150.12','SP','Paulina','2022-12-01 11:52:22.086572-03','2022-12-01 11:52:22.086572-03'),
	 ('e6bd659b555f8b306188ce2c9733b7b5096d84312ca81e86c220dccb2fab','RACKS REFRIGERACAO LTDA','00547437000140','juridica','fabiola brandão','189483.0','PR','Curitiba','2022-12-01 11:52:22.090309-03','2022-12-01 11:52:22.090309-03'),
	 ('e3d7abbe80dac2bd249c13cf9686a42c159edcc589b163ad9aa3f9631c00','Auto Postos Brittos Ltda','00548444000166','juridica','J.S. Santos Produtora Artística & Literária','5852.14','MG','Varginha','2022-12-01 11:52:22.091685-03','2022-12-01 11:52:22.091685-03'),
	 ('230100f0b6ea1711eac544711844ff4a1dc9213b81507e8c1cb3556b68e4','Orca Veiculos Ltda','00549675000194','juridica','','52000.0','DF','Brasília','2022-12-01 11:52:22.093002-03','2022-12-01 11:52:22.093002-03'),
	 ('ad7a715927246543437254b1d1f22a365e4eee3e306a4d26f1cfbd6016a9','NETAFIM BRASIL SISTEMAS E EQUIPAMENTOS DE IRRIGACAO LTDA.','00549740000181','juridica','Sergio Andrés Lulkin','40000.0','SP','Ribeirão Preto','2022-12-01 11:52:22.094267-03','2022-12-01 11:52:22.094267-03'),
	 ('4ccc37125212a8b0321c4f287cec708c19136c2f8eedf345f2ab58934d0b','Casa Blanca Comunicações e Marketing Ltda','00553702000100','juridica',' ','900.0','MG','Belo Horizonte','2022-12-01 11:52:22.095519-03','2022-12-01 11:52:22.095519-03'),
	 ('ac5dfe7889574568e1cac7455fc62ff43ac9d8854eff9ef38c0e3b6f3a22','DIMAV DIMAP Veículos Ltda','00553764000104','juridica',' ','1000.0','MG','Ipatinga','2022-12-01 11:52:22.096758-03','2022-12-01 11:52:22.096758-03'),
	 ('83a788c4b3d6a658bd2d4358a8fd3c0a4eaf2d7d08949ce5f1576e0f55ff','Barugui S.A. Crédito, Financiamentos e Investimentos','00556603000174','juridica','','456400.0','PR','Curitiba','2022-12-01 11:52:22.098038-03','2022-12-01 11:52:22.098038-03'),
	 ('e5b4fcca53bf91f1fd811c2ce3fcc36186126639d00dd895534838e73607','Interbrasil Comercial Exportadora S.A.','00557713000150','juridica','','78395.89','SC','São Bento do Sul','2022-12-01 11:52:22.0993-03','2022-12-01 11:52:22.0993-03'),
	 ('f412ca509164f822d143c7fd0634c638ab6c1445c10a7582807009f53663','Banco BGN S.A','00558456000171','juridica','','757511.0','PE','Recife','2022-12-01 11:52:22.100499-03','2022-12-01 11:52:22.100499-03');
