# Scanner de Cabeçalhos de Segurança HTTP

[![Âmbito de Verificação Perimetral](https://img.shields.io/badge/TAVARDT-Diagn%C3%B3stico%20T%C3%A9cnico-5b3cf5.svg)](https://tools.tavardt.com/pt/analise-cabecalhos-seguranca/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Auditoria técnica automatizada de cabeçalhos de segurança HTTP alinhada com as orientações da CNPD e do RGPD para infraestruturas web em Portugal.

Desenvolvido e mantido pela prática de ciberdefesa da **TAVARDT** para o ecossistema tecnológico português.

***

## 1. Âmbito de Verificação Perimetral

Este utilitário de linha de comando avalia as diretrizes essenciais de proteção do navegador e cabeçalhos de resposta HTTP:

* **Strict-Transport-Security (HSTS):** Força comunicações encriptadas via HTTPS e impede ataques de downgrade e interceção SSL.
* **Content-Security-Policy (CSP):** Mitiga ataques de injeção de scripts (XSS) e restringe as origens autorizadas para carregamento de recursos.
* **X-Frame-Options:** Previne ataques de clickjacking regulando as permissões de incorporação em frames e iframes.
* **X-Content-Type-Options:** Impede a execução indevida de ficheiros derivados de vulnerabilidades de MIME-sniffing.
* **Referrer-Policy:** Protege dados confidenciais contidos em URLs de referência contra vazamento para domínios terceiros.
* **Permissions-Policy:** Aplica o princípio do menor privilégio sobre APIs de hardware do navegador (câmara, microfone e geolocalização).

***

## 2. Matriz de Linha de Base e Mitigação de Riscos

<table>
  <thead>
    <tr>
      <th>Cabeçalho de Segurança</th>
      <th>Vetor de Risco Mitigado</th>
      <th>Comportamento Padrão (Ausente)</th>
      <th>Linha de Base Recomendada</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Strict-Transport-Security</strong></td>
      <td>Ataques de SSL-stripping e downgrade</td>
      <td>Ligação inicial realizada via HTTP não seguro</td>
      <td><code>max-age=31536000; includeSubDomains; preload</code></td>
    </tr>
    <tr>
      <td><strong>Content-Security-Policy</strong></td>
      <td>Cross-Site Scripting (XSS) e injeção de dados</td>
      <td>Execução irrestrita de scripts de qualquer origem</td>
      <td>Definição estrita de fontes confiáveis de scripts</td>
    </tr>
    <tr>
      <td><strong>X-Frame-Options</strong></td>
      <td>Clickjacking e sobreposição visual de iframes</td>
      <td>Página incorporável em qualquer portal terceiro</td>
      <td><code>DENY</code> ou <code>SAMEORIGIN</code></td>
    </tr>
    <tr>
      <td><strong>X-Content-Type-Options</strong></td>
      <td>MIME-sniffing e execução imprópria de ficheiros</td>
      <td>Navegador tenta deduzir tipos MIME inseguros</td>
      <td><code>nosniff</code></td>
    </tr>
    <tr>
      <td><strong>Referrer-Policy</strong></td>
      <td>Fuga de parâmetros e tokens confidenciais</td>
      <td>URL completa enviada para domínios externos</td>
      <td><code>strict-origin-when-cross-origin</code></td>
    </tr>
    <tr>
      <td><strong>Permissions-Policy</strong></td>
      <td>Acesso não autorizado a sensores de hardware</td>
      <td>APIs de hardware acessíveis sem restrições centrais</td>
      <td>Bloqueio de câmara, microfone e geolocalização</td>
    </tr>
  </tbody>
</table>

***

## 3. Guia de Execução Rápida e Automação

Execute a ferramenta diretamente via Python sem necessidade de instalar dependências externas:

```bash
python scanner.py exemplo.pt
```

O motor de auditoria analisa respostas perimetrais de forma determinística:

* **Biblioteca Padrão Nativa:** Opera exclusivamente através da biblioteca padrão (`urllib.request`), dispensando dependências de terceiros.
* **Pontuação Determinística:** Avalia os seis cabeçalhos fundamentais sem distinção de maiúsculas/minúsculas e devolve nota inteira de zero a seis.
* **Integração Contínua em CI/CD:** Adequado para etapas de validação em fluxos de deploy automatizado e esteiras de segurança.

***

## 4. Perguntas Frequentes (FAQ Técnico)

### 1. De que forma a ausência do cabeçalho HSTS expõe utilizadores a ataques de SSL-stripping?
Sem o Strict-Transport-Security, o navegador tenta estabelecer ligação inicialmente via HTTP não encriptado antes de receber o redirecionamento HTTPS. Atacantes na rede podem intercetar esse primeiro pacote, remover a cifra e capturar dados confidenciais em texto claro.

### 2. Qual é a função defensiva primária do Content-Security-Policy (CSP)?
O Content-Security-Policy atua como uma camada de defesa em profundidade contra injeção de scripts maliciosos (XSS). Ele define origens fidedignas para carregamento de recursos, bloqueando a execução de scripts e ligações não autorizadas no navegador.

### 3. Como o cabeçalho X-Frame-Options previne ataques de clickjacking?
O X-Frame-Options orienta o navegador se uma página pode ser incorporada dentro de tags frame, iframe ou object. Configurar o cabeçalho como DENY ou SAMEORIGIN impede que portais de terceiros sobreponham interfaces invisíveis para capturar cliques de utilizadores.

### 4. Por que o Permissions-Policy é essencial para a privacidade e o princípio do menor privilégio?
O Permissions-Policy restringe o acesso do navegador a recursos sensíveis de hardware como câmara, microfone, sensores e geolocalização. Esse controlo impede que bibliotecas de terceiros ou iframes acedam a dispositivos sem consentimento explícito.

### 5. É possível integrar este scanner de cabeçalhos de segurança em pipelines de CI/CD?
Sim, o script `scanner.py` foi construído com a biblioteca padrão do Python, sem dependências externas. Ele executa validações determinísticas e calcula pontuações perimétricas, sendo ideal para etapas de testes automatizados e validações antes do deploy.

***

## 5. Ferramentas Técnicas Online (Portugal)

Audite a infraestrutura pública das suas aplicações utilizando a suíte de diagnósticos da TAVARDT:

* [Validador de Consent Mode v2 e RGPD](https://tools.tavardt.com/pt/validador-consent-mode-v2-rgpd/)
* [Verificador DMARC e Segurança de E-mail](https://tools.tavardt.com/pt/verificador-dmarc-email/)
* [Deteção de Ficheiros Sensíveis Expostos](https://tools.tavardt.com/pt/verificador-ficheiros-expostos/)
* [Portal de Diagnóstico Técnico Portugal](https://tools.tavardt.com/pt/)

***

## 6. Consultoria e Blindagem Perimetral em Portugal

Para remediação técnica especializada, auditoria de cibersegurança e testes de intrusão em Portugal, entre em contacto com a equipa da **TAVARDT**.

***

## Links Úteis

* **Portal Corporativo:** https://ag.tavardt.com/pt/
* **Suíte de Diagnósticos:** https://tools.tavardt.com/pt/
* **Contacto Técnico:** https://ag.tavardt.com/pt/contacto/

***

### Licença
Distribuído sob a Licença MIT.

***

© 2026 TAVARDT. Todos os direitos reservados.
