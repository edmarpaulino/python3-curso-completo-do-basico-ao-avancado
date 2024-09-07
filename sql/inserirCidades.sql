insert into cidades (nome, area, estado_id)
values ('Campinas', 795, 26);

select * from estados where id = 26;

select * from estados;

insert into cidades (nome, area, estado_id)
values ('Niterói', 133.9, 20);

update cidades set estado_id = 20 where nome = 'Niterói';

insert into cidades (nome, area, estado_id)
values ('Caruaru', 920.6, (select id from estados where sigla = 'PE'));

insert into cidades (nome, area, estado_id)
values ('Juazeiro do Norte', 248.2, (select id from estados where sigla = 'CE'));

select * from cidades;