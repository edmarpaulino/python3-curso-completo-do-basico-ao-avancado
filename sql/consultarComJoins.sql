select * from prefeitos;
select * from cidades;

select * from cidades c inner join prefeitos p on c.id = p.cidade_id;
select * from cidades c left outer join prefeitos p on c.id = p.cidade_id;
select * from cidades c right outer join prefeitos p on c.id = p.cidade_id;
-- select * from cidades c full outer join prefeitos p on c.id = p.cidade_id;

select * from cidades c left outer join prefeitos p on c.id = p.cidade_id
union
select * from cidades c right outer join prefeitos p on c.id = p.cidade_id;