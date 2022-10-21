
# instalação do driver para conexão com o Mysql
!pip install mysql-connector

# importação do driver para conexão com o Mysql
import mysql.connector

# conexão com o servidor 
conn = mysql.connector.connect( host = "localhost", user = "root", passwd = "senhaaqui" )

# Cria o banco de dados
cursor = conn.cursor()
cursor.execute("create database empresa")


# Comandos em banco MySql com Python


# Coloca o banco de dados em uso 
cursor = conn.cursor()
cursor.execute("use empresa")

# Cria tabela funcionários 
cursor.execute("create table funcionarios(id_funcionario   int not null,nome_funcionario  varchar(40) not null,cargo             varchar(20),primary key(id_funcionario))")

# Cria tabela dependentes
cursor.execute("create table dependetes(id_dependente   int not null,id_funcionario  int not null,nome_dependente varchar(40),parentesco      varchar(40) not null,primary key(id_dependente),foreign key(id_funcionario) references funcionarios(id_funcionario))")

# Mostra tabela
cursor.execute("show tables")
tables = cursor.fetchall()
count = 0
max = len(tables)
for i in tables:
    cursor.execute("DESCRIBE " + i[0])
    table = cursor.fetchall()
    print("Tabela: " + i[0])
    for j in table:
        print(
            "Atributo: " + j[0] +
            " - Tipo: " + str(j[1].decode("utf-8"))
        )
    count += 1
    if count < max:
        print("")


# Insere registros na tabela 
cursor = conn.cursor()
cursor.execute("use empresa")
cursor = conn.cursor()
cursor.execute("insert into funcionarios (id_funcionario, nome_funcionario, cargo)values('1', 'André', 'Auxiliar')")

# commit 
conn.commit()
print(cursor.rowcount, "registro inserido.")

# Insere registros na tabela
nomes = [
    'Pedrão',
    'Zezinho',
    'Joãozinho',
    'Zezão',
    'Zezinho',
    'Juca',
    'Juquinha'
]
cargos = [
    'Gerente',
    'Diretor',
    'Presidente',
    'Vice-Presidente',
    'Diretor',
    'Gerente',
    'Diretor'
]
qry = """
    INSERT INTO funcionarios
    (nome_funcionario, cargo) VALUES
    (%s, %s)
"""
for i in range(len(nomes)):
    vls = (nomes[i], cargos[i])
    cursor.execute(qry, vls)

dados = [('Bernadete', 'Farmacêutica'), ('Joana', 'Enfermeira')]
cursor.executemany(qry, dados)

nome = input("Informe o nome do cidadão: ")
cargo = input("Informe o cargo do cidadão: ")
cursor.execute(qry, (nome, cargo))

# Select na tabela
cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()
print("Tabela de funcionários:")
for i in funcionarios:
    print(i)

# Inserindo campos na tabela dependentes 
qry = """
    INSERT INTO dependentes
    (id_funcionario, nome, parentesco)
    VALUES
    (%s, %s, %s)
"""

nome = input("Informe o nome do dependente: ")
funcionario = input("Informe o nome do funcionário: ")
parentesco = input("Informe o parentesco do depentente em relação ao funcionário: ")

cursor.execute(f"""
    SELECT id_funcionario FROM funcionarios
    WHERE nome_funcionario = '{funcionario}'
""")
id_funcionario = cursor.fetchall()
if id_funcionario != []:
    vls = (id_funcionario[0][0], nome, parentesco)
    cursor.execute(qry, vls)
else:
    print("Funcionário não existe na empresa.")

# Select na tabela de dependentes 
print("Tabela de dependentes:")
cursor.execute("SELECT * FROM dependentes")
dependentes = cursor.fetchall()
for i in dependentes:
    print(i)

# Resultado Final
print("\nTabela dos funcionários com dependentes:")
cursor.execute("""
    SELECT funcionarios.nome_funcionario, dependentes.nome_dependente, dependentes.parentesco
    FROM funcionarios, dependentes
    WHERE funcionarios.id_funcionario = dependentes.id_funcionario
""")
relacoes = cursor.fetchall()
for i in relacoes:
    print(i)