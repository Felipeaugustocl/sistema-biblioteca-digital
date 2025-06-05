Guia de Contribuição para o Projeto Biblioteca Digital
Para garantir um processo de desenvolvimento organizado e eficiente, pedimos que siga estas diretrizes.

Como Contribuir
Existem várias maneiras de contribuir para este projeto:

Reportando bugs

Sugerindo novas funcionalidades ou melhorias

Escrevendo código para corrigir bugs ou implementar funcionalidades

Melhorando a documentação

Configuração do Ambiente de Desenvolvimento (Sugestão)
Faça um Fork do Repositório: Clique no botão "Fork" no canto superior direito da página do repositório no GitHub. Isso criará uma cópia do projeto na sua conta do GitHub.

Clone o seu Fork: No seu computador, clone o repositório que você acabou de "forkar":

git clone https://github.com/SEU_NOME_DE_USUARIO/sistema-biblioteca-digital.git
cd sistema-biblioteca-digital

Adicione o Repositório Original como "Upstream": Isso permite que você mantenha seu fork sincronizado com o projeto principal.

git remote add upstream https://github.com/Felipeaugustocl/sistema-biblioteca-digital.git

Crie um Branch para suas Alterações: Nunca trabalhe diretamente no branch master (ou main) do seu fork. Crie um novo branch para cada funcionalidade ou correção:

git checkout -b nome-descritivo-do-seu-branch

Exemplos: feat/adiciona-busca-avancada ou fix/corrige-erro-listagem.

Fazendo Alterações e Commits
Escreva seu Código: Faça as alterações ou adições desejadas no código.

Teste suas Alterações: Certifique-se de que seu código funciona como esperado e não introduz novos problemas.

Adicione suas Alterações ao Staging Area:

git add .

(ou git add nome_do_arquivo_especifico)

Faça o Commit das suas Alterações: Use mensagens de commit claras e descritivas. Siga o padrão de "Conventional Commits" se possível (ex: feat: ..., fix: ..., docs: ...).

git commit -m "Tipo: Breve descrição da alteração"

Exemplo:

git commit -m "feat: Adiciona funcionalidade de busca por autor"

Ou

git commit -m "fix: Corrige erro de digitação na mensagem de boas-vindas"

Enviando suas Alterações (Push)
Envie o seu branch para o seu fork no GitHub:

git push origin nome-descritivo-do-seu-branch

Criando um Pull Request (PR)
Abra um Pull Request: Vá para a página do seu fork no GitHub. Você verá um botão para "Compare & pull request" para o branch que você acabou de enviar. Clique nele.

Descreva seu Pull Request:

Verifique se o "base repository" é o Felipeaugustocl/sistema-biblioteca-digital e o "base branch" é master (ou main).

O "head repository" deve ser o seu fork e o "compare branch" deve ser o nome-descritivo-do-seu-branch.

Escreva um título claro e uma descrição detalhada do que você fez no seu Pull Request. Explique o problema que você está resolvendo ou a funcionalidade que está adicionando. Se houver uma "Issue" relacionada, mencione-a (ex: Closes #123).

Submeta o Pull Request: Clique em "Create pull request".

Revisão do Pull Request
Os mantenedores do projeto revisarão seu PR.

Podem ser solicitadas alterações ou feitos comentários. Responda às solicitações e faça os ajustes necessários no seu branch, fazendo novos commits e pushs para o mesmo branch (o PR será atualizado automaticamente).

Uma vez aprovado, seu PR será mesclado ao projeto principal.

Mantendo seu Fork Sincronizado
Antes de criar um novo branch para uma nova contribuição, é uma boa prática sincronizar seu fork com o repositório original:

Mude para o seu branch principal local (geralmente master ou main):

git checkout master

Busque as alterações do repositório upstream:

git fetch upstream

Faça o merge das alterações do upstream/master no seu master local:

git merge upstream/master

Envie as atualizações para o seu master no GitHub (seu fork):

git push origin master

Obrigado por contribuir!