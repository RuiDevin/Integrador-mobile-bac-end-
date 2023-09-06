
# Projeto Integrador - Ruivo Solutions

Professores: Marco André Mendes e Alann Perini.

Projeto feito por Rafael Alvaro Almeida

# Situação Problema

Rafael possui um negócio de manutenção de celulares,  desktops e notebooks. Ele deseja que seja desenvolvido para o seu negócio, um sistema de ORDEM DE SERVIÇO afim de uniformizar, otimizar e administrar sua empresa.

Rafael, especialista em reparos de aparelhos eletrônicos, estabelece contato com os clientes através de mensagens eletrônicas ou encontros pessoais, a fim de oferecer orçamentos sem compromisso. Embora os potenciais clientes descrevam o problema que estão enfrentando, Rafael sempre realiza uma inspeção minuciosa no aparelho eletrônico para confirmar a origem e a gravidade do defeito.

Uma vez identificado o problema, Rafael pesquisa os componentes eletrônicos necessários para o reparo, verificando os preços e prazos de entrega. Em seguida, ele entra em contato com o cliente, informando o valor do conserto e o prazo estimado para solucionar o problema do aparelho. 

Para oferecer opções aos clientes, Rafael realiza pesquisas no mercado local, nacional e internacional, apresentando pelo menos dois ou três orçamentos diferentes. Caso o cliente aceite o orçamento proposto, Rafael encomenda as peças e realiza o reparo necessário. 

Ao concluir o trabalho, ele notifica o cliente de que o aparelho está pronto e disponível para retirada. Rafael oferece uma garantia de três meses para os reparos realizados nos aparelhos eletrônicos, exceto para serviços de limpeza. Ele registra as garantias dos serviços em notas fiscais de compra dos componentes utilizados, uma vez que as peças adquiridas possuem garantia de três meses oferecida pelo fabricante ou distribuidora. 

No caso de algum cliente reclamar que o aparelho eletrônico não está funcionando corretamente após o reparo, Rafael analisa o problema e busca encontrar uma solução adequada. 

Se o cliente não aceitar o orçamento proposto, Rafael devolve o aparelho nas mesmas condições em que foi recebido, caso seja possível, e o cliente pode ir buscá-lo.

# Descrição da proposta

A proposta é desenvolver um software que visa automatizar e facilitar o serviço de assistência técnica oferecido por Rafael, abordando diversos aspectos do negócio, como gerenciamento de vendas, gastos, garantias e o acompanhamento do andamento dos serviços.

O software será projetado para atender tanto o gestor do negócio quanto os funcionários da assistência técnica. Cada nível de usuário terá acesso a recursos e funcionalidades específicas, de acordo com suas responsabilidades e necessidades.

Para o gestor, o software fornecerá uma visão geral do desempenho da assistência técnica, permitindo o acompanhamento das vendas realizadas, dos gastos incorridos e das garantias em vigor. Ele também poderá monitorar o andamento dos serviços, verificar o status de cada caso e tomar medidas adequadas para garantir a satisfação dos clientes.

Já para os funcionários, o software oferecerá recursos para registrar as vendas realizadas, inserir os gastos incorridos, cadastrar e gerenciar as garantias dos produtos e atualizar o status dos serviços em andamento. Também poderá disponibilizar uma agenda de atendimentos, facilitando a organização e o planejamento das atividades diárias.

# Regras de negócio

TODO: REVISAR ORTOGRAFIA E FORMATO

**RN001 - Cadastro de cliente:** O cliente fará seu cadastro na loja preenchendo um formulário com informações cruciais para sua identificação.

**RN002 - Descrição do problema:** O software apresentará uma tela para o cliente, onde ele poderá fazer a descrição do problema com um campo para inserção de fotos e vídeos do aparelho eletrônico em questão.

**RN003 - Geração da ordem de serviço:** O sistema deverá gerar uma ordem de serviço quando o cliente cadastrado deixar seu aparelho eletrônico na assistência. A ordem de serviço conterá informações como qual aparelho é, quando o aparelho entrou e o número da Ordem de Serviço (OS).

**RN004 - Detalhamento do problema:** Após o aparelho ser entregue à assistência, será gerada uma ordem de serviço contendo a descrição detalhada do problema.

**RN005 - Orçamento:** Antes de realizar qualquer serviço, a assistência técnica deve informar ao cliente o valor do reparo após a examinação do aparelho.

**RN006 - Barra de progresso:** Será gerada uma barra de progresso, utilizando o número da ordem de serviço, para acompanhar os estágios do aparelho eletrônico, como Em fila, Próximo da fila, Em examinação, Orçamento disponível, Em reparo e Disponível para retirada.

**RN007 - Garantia de serviço:** Após a conclusão do reparo e o recebimento do pagamento, será gerada uma garantia de serviço de 90 dias, contendo o valor do reparo e a data de saída do aparelho.

# Requisitos funcionais

**RF001 (Cadastro de clientes):**
**Descrição:** O sistema deve permitir que o cliente se cadastre para ter acesso aos serviços.
**Dados necessários:** Nome, endereço, telefone, e-mail, senha.

**Usuários:** Todos os níveis de usuário.

**RF002 (Acesso ao sistema):**
**Descrição:** O sistema deve permitir diferentes níveis de acesso aos usuários. O administrador terá acesso a todas as informações, o atendente terá acesso a algumas áreas específicas e o cliente terá acesso apenas à sua área pessoal.
**Dados necessários:** Nível de acesso (administrador, atendente, cliente), dados de autenticação (usuário e senha).

**Usuários:** Administrador, atendente, cliente.

**RF003 (Primeiro contato):**
**Descrição:** O sistema deve permitir que os clientes entrem em contato com a assistência técnica por meio de mensagens eletrônicas ou pessoalmente, para solicitar orçamentos para seus aparelhos eletrônicos.
**Dados necessários:** Mensagem do cliente, informações de contato.

**Usuários:** Cliente.

**RF004 (Geração de ordem de serviço):**
**Descrição:** O sistema deve permitir que o atendente gere uma ordem de serviço para o cliente.
**Dados necessários:** Informações do cliente, descrição do problema.

**Usuários:** Atendente.

**RF005 (Código de acompanhamento):
**Descrição:** O sistema deve permitir que seja gerado um código na ordem de serviço para possibilitar o acompanhamento do serviço.
**Dados necessários:** Código de acompanhamento, número da ordem de serviço.

**Usuários:** Todos os níveis de usuário.

**RF006 (Acompanhamento em tempo real):**
**Descrição:** O sistema deve exibir uma barra de status do serviço com base no código de acompanhamento, permitindo acompanhar em tempo real o estágio do aparelho eletrônico (Em fila, Próximo da fila, Em exame, Orçamento disponível, Em reparo, Disponível para retirada).
**Dados necessários:** Código de acompanhamento.

**Usuários:** Todos os níveis de usuário.

**RF007 (Avisos prévios):**
**Descrição:** O sistema deve permitir que o atendente se comunique com o cliente para informar sobre quaisquer alterações fora do esperado ou combinado.
**Dados necessários:** Mensagem do atendente, informações de contato do cliente.

**Usuários:** Atendente, cliente.

**RF008 (Não aprovação orçamentária):**
**Descrição:** O sistema deve permitir que, caso o orçamento não seja aprovado pelo cliente, o aparelho seja separado em um local específico para ser recolhido pelo dono do aparelho, apenas com a apresentação da ordem de serviço ou do código.
**Dados necessários:** Status do orçamento, número da ordem de serviço ou código.

**Usuários:** Atendente, cliente.

**RF009 (Reparo concluído):**
Descrição: O sistema deve permitir a geração de uma nota fiscal com garantia de 90 dias do serviço, após o pagamento integral do reparo.
Dados necessários: Informações do cliente, valor do reparo, data de pagamento.

**Usuários:** Atendente.

# Requisitos não funcionais

**RNF001 - Segurança:** O formulário preenchido pelo cliente deve garantir a privacidade e segurança dos dados fornecidos.

**RNF002 - Usabilidade:** A interface do software deve ser amigável e intuitiva para permitir que o cliente descreva com clareza o problema com seu aparelho eletrônico.

**RNF003 - Confiabilidade:**O sistema deve gerar corretamente a ordem de serviço com as informações relevantes, como aparelho, data de entrada e número da ordem de serviço.

**RNF004 - Escalabilidade:**O sistema deve ser capaz de gerar ordens de serviço para um grande número de clientes sem comprometer a eficiência.

**RNF005 - Transparência:** A assistência técnica deve informar ao cliente o valor do reparo antes de realizar qualquer serviço.

**RNF006 - Rastreabilidade:** O sistema deve fornecer uma barra de progresso para que o cliente possa acompanhar o andamento do reparo do seu aparelho eletrônico.

**RNF007 - Confiabilidade:** O sistema deve gerar corretamente a garantia de serviço de 90 dias, contendo o valor do reparo e a data de saída do aparelho.
