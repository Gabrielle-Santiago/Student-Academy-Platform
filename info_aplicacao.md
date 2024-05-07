# Informações sobre a construção da aplicação

## Conceito Geral
<p> O Student Academy Plataform é uma plataforma que oferece cursos, tutoriais e mentorias em diversas habilidades digitais, como programação, design gráfico, marketing digital e análise de dados, visando capacitar indivíduos para o mercado de trabalho digital. Para saber mais sobre o intuito da aplicação clique aqui (https://github.com/Gabrielle-Santiago/Student-Academy-Platform/blob/0c065f38d254d1c8ee412c60f8d25d72fbcb5f94/README.md). </p>

## Tecnologias Utilizadas
### Linguagens de Programação:
* Python: Utilizado na criação da aplicação desktop devido à sua flexibilidade e vasta gama de bibliotecas e frameworks.
* JavaScript: Empregado nas interações dinâmicas no lado do cliente.
* HTML/CSS: Utilizados para a estruturação e estilização da interface do usuário (UI) da aplicação web.

### Frameworks e Bibliotecas:
* Kivy: Biblioteca utilizada para desenvolvimento da aplicação que faz parte da interface do usuário final.

### Ferramentas e Plataformas:
* Git: Sistema de controle de versão utilizado para gerenciar e controlar o código fonte da aplicação.
* GitHub: serviço de hospedagem na Web para repositórios do Git.

### Sistema Operacional:
* Windows: Sistema operacional utilizado pela grande maioria dos usuários, que possui um sistema de interface gráfica multitarefa.

## Arquitetura e Estrutura
### Descrição Geral:
<p> A aplicação de projeto estudantil é projetada seguindo uma arquitetura baseada em microserviço, dividida em componentes e módulos que interagem entre si, com intuito de oferecer funcionalidades robustas e escaláveis. </p>

### Componentes e Módulos:
* Módulo de Autenticação: Responsável pela autenticação, autorização e gestão de usuários.
* Módulo de Cursos: Gerencia informações, nível de dificuldade, categorias e detalhes dos cursos.
* Módulo de Gerencia: Processa e gerencia a inclusão e exclusão dos cursos do perfil do usuário.
* Módulo de Comunicação: Permite a interação de usuários com intuito de expor conhecimento entre os mesmos.
* Módulo de Perguntas: Permite resolução de questionamentos com a comunidade ou suporte técnico.

### Camadas e Serviços:
* Camada de Apresentação: Interface do usuário, páginas web, aplicativo desktop e interfaces de usuário.
* Camada de Lógica de Negócios: Regras de negócios, lógica de processamento, validações e cálculos.
* Camada de Acesso a Dados: Banco de dados, armazenamento, e serviços de persistência.

### Diagrama UML:
1.	Diagrama de Classes:
* Descrição: Este diagrama representa a estrutura estática do sistema, mostrando as classes, seus atributos, métodos e relacionamentos.
Elementos Chave:
#### Usuário 
* O usuário inicia na tela de login, na qual deve ser fornecido suas credenciais, à mesma tem uma conexão obrigatória (<<include>>) com o método cadastrado.
* A classe Cadastro registra os dados principais do usuário e lança no banco de dados (Associação ->).
* A classe Esqueci Senha, envia um código de recuperação (<<include>>), e aguarda a confirmação do mesmo, após permite que o usuário refaça sua senha (Associação ->).
* Após o envio das credenciais na área de login o usuário está logado na aplicação.

#### Usuário Logado
* A classe Perfil está vinculada à atualização de dados (Associação ), e a exclusão caso o mesmo exista (<<extend>>).
* A classe Cursos foca na visualização clara e direta dos cursos disponibilizados, a qual possui a classe Atividades vinculada (Composição) que necessita diretamente da classe Cursos para existir, e a classe Atividade Finalizadas depende do termino de uma atividade (Dependência -->).
* A classe Navegação tem por finalidade explorar as funcionalidades da aplicação.
* A classe Matricular no Curso tem conexão com a classe Navegação (Associação ->) que tem intuito de matricular o usuário no curso desejado. E a classe Confirmação do Usuário tem vínculo com a classe Matricular no curso (), com finalidade de garantir que o usuário compreenda as responsabilidades subsequentes. 
* E a classe Acessar Curso (Dependência -->), encaminha o usuário para a página referente ao curso.
* A classe Comunidade tem por intuito disponibilizar uma área para os usuários interagirem entre si, à mesma possui conexão com as classes Visualizar Conversas Anteriores e Responder Interações (Associação ->).
* A classe Trilhas possui o objetivo de auxiliar o usuário a selecionar o melhor método para estudar, diante disso, a classe Escolher um Nível está associada à mesma (Associação ). 
* E a classe Cursos e Atividade tem função de após escolhido o nível mostrar o resultado correspondente (Dependência -->).
* A classe Artigo dispõe duas opções a primeira é o usuário escolher um curso e o mesmo será encaminhado para os artigos referentes por meio da classe Escolher Curso (Associação ) e Encaminhar Artigos (Associação ->).
* E a segunda é o usuário visualizar os artigos sem um curso referente, por meio da classe Visualizar Artigos Aleatórios (Associação ->)
* A classe Perguntas Frequentes envia para a classe de Aba de perguntas frequentes (Associação ->), a qual possui duas alternativas
* A primeira alternativa é uma conexão da classe Perguntar para comunidade à classe regente (Agregação), onde será redirecionado para a comunidade.
* A segunda alternativa é a classe Contato com Suporte que está conectada com a classe regente de forma obrigatória para continuar (<<include>>), em seguida o usuário terá um retorno por meio da classe Retorna da Pergunta (Dependência -->).

![aplicacao](C:\Users\User\OneDrive\Área de Trabalho\Projeto Estácio\Documentacao\Modelagem UML\Student Academy Platform.jpg)

Exemplo Prático:
<p> O usuário realiza o cadastro, fornecendo todas as informações necessárias, e após confirmação que seu cadastro foi registrado no banco de dados, o mesmo, retorna para a área de login e informa suas respectivas credenciais. </p>
<p> Na aplicação o usuário tem diversas alternativas a seguir, mas no exemplo seguiremos a sequência da descrição do diagrama UML. O usuário clica na área referente ao perfil e atualiza os dados, como número de contato, ou o mesmo decide excluir um curso que havia se matriculado anteriormente. Após isso decide ir na área de cursos para visualizar quais ainda faltam terminar e suas respectivas atividades, ao finalizar suas pendências, o mesmo visita a área de navegação e analisa os cursos, e qual se encaixa na suas preferencias, ao selecionar um novo curso, uma tela de confirmação aparece, informando que será encaminhado para uma nova aba, visando que os cursos são disponibilizados por outras plataformas, e que a aplicação é um mediador das informações. </p>
<p> Após confirmar será encaminhado para a área do curso, onde realizará o cadastro em outra plataforma, e se associará ao curso selecionado. </p>
<p> Em seguida o usuário decide visitar a comunidade para interagir, na mesma pode ler as conversas e conversar em tempo real, quando retira-se dessa área opta por escolher uma trilha para obter um melhor desenvolvimento em seu curso, à qual é subdivida entre três níveis: fácil, médio e difícil.
Em função de aprofundar seus conhecimentos o usuário decide ir para a área de artigos, onde tem a opção de escolher artigos sobre um curso de preferencia ou ler artigos aleatórios. </p>
<p> Para finalizar o usuário pretende realizar um questionamento, e para isso abre a área de perguntas frequentes, na mesma possui duas opções, onde pode fazer o questionamento para a comunidade ou entrar em contato com o suporte técnico. O mesmo decide contatar o suporte técnico, que pede para formular o questionamento e escolher o meio de envio, à qual pode ser Email, chat ou telefone, o envio será realizado e uma confirmação aparecerá, após um prazo predeterminado o suporte técnico responderá ao questionamento e será enviado para o usuário. </p>

#### Interfaces e Fluxos de Dados:
<p> As interfaces são projetadas para serem intuitivas, responsivas e amigáveis, permitindo aos usuários navegar, pesquisar e visualizar conteúdos facilmente. Os fluxos de dados são otimizados para eficiência, segurança e desempenho, garantindo a transmissão, processamento, armazenamento e gerenciamento adequado das informações. </p>
