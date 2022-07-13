import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class Qual_Palavra(App):
    a = 0
    def Sortear(self, instance):
        self.Palavras_5letras=['abade', 'abafa', 'abafe', 'abafo', 'abafa', 'abala', 'abale', 
                              'abalo', 'abala', 'abana', 'abane', 'abano', 'abana', 'abata', 
                              'abate', 'abati', 'abato', 'abate', 'abeto', 'ablua', 'ablui', 
                              'abluo', 'ablui', 'abole', 'aboli', 'abono', 'abram', 'abras', 
                              'abrem', 'abres', 'abreu', 'abria', 'abril', 'abrir', 'abris', 
                              'abriu', 'abste', 'abusa', 'abuse', 'abuso', 'abusa', 'acaba', 
                              'acabe', 'acabo', 'acaba', 'acaso', 'acata', 'acate', 'acato', 
                              'acata', 'acena', 'acene', 'aceno', 'acena', 'acesa', 'aceso', 
                              'aceto', 'achai', 'acham', 'achar', 'achas', 'achei', 'achem', 
                              'aches', 'achou', 'acima', 'acode', 'acola', 'acuai', 'acuam', 
                              'acuar', 'acuas', 'acuda', 'acudi', 'acudo', 'acuei', 'acuem', 
                              'acues', 'acuou', 'acusa', 'acuse', 'acuso', 'acusa', 'adaga', 
                              'adega', 'adere', 'aderi', 'adeus', 'adiai', 'adiam', 'adiar', 
                              'adias', 'adida', 'adido', 'adiei', 'adiem', 'adies', 'adimo', 
                              'adiou', 'adira', 'adiro', 'adira', 'adita', 'adite', 'adito', 
                              'adita', 'adoce', 'adora', 'adore', 'adoro', 'adora', 'adota', 
                              'adote', 'adoto', 'adota', 'adoca', 'adoco', 'adoca', 'aduba', 
                              'adube', 'adubo', 'aduba', 'adula', 'adule', 'adulo', 'adula', 
                              'advim', 'advir', 'advem', 'afaga', 'afago', 'afaga', 'afana', 
                              'afane', 'afano', 'afana', 'afega', 'afere', 'aferi', 'afeta', 
                              'afete', 'afeto', 'afeta', 'afiai', 'afiam', 'afiar', 'afias', 
                              'afiei', 'afiem', 'afies', 'afina', 'afine', 'afino', 'afins', 
                              'afina', 'afiou', 'afira', 'afiro', 'afixa', 'afixe', 'afixo', 
                              'afixa', 'aflua', 'aflui', 'afluo', 'aflui', 'afoba', 'afobe', 
                              'afobo', 'afoba', 'afofa', 'afofe', 'afofo', 'afofa', 'afoga', 
                              'afogo', 'afoga', 'afora', 'afore', 'aforo', 'afora', 'afros', 
                              'aftas', 'agiam', 'agias', 'agido', 'agimo', 'agira', 'agira', 
                              'agita', 'agite', 'agito', 'agita', 'agora', 'aguai', 'aguam', 
                              'aguar', 'aguas', 'aguce', 'aguda', 'agudo', 'aguei', 'aguem', 
                              'agues', 'aguou', 'aguca', 'aguco', 'aguca', 'ainda', 'aires', 
                              'ajais', 'ajamo', 'ajuda', 'ajude', 'ajudo', 'ajuda', 'alada', 
                              'alado', 'alaga', 'alago', 'alaga', 'alcei', 'alcem', 'alces', 
                              'aldea', 'alega', 'alego', 'alega', 'alema', 'algas', 'algoz', 
                              'algum', 'alhea', 'alhos', 'aliai', 'aliam', 'aliar', 'alias', 
                              'aliei', 'aliem', 'alies', 'alija', 'alije', 'alijo', 'alija', 
                              'aliou', 'alisa', 'alise', 'aliso', 'alisa', 'alias', 'almas', 
                              'aloca', 'aloco', 'aloca', 'aloja', 'aloje', 'alojo', 'aloja', 
                              'aloes', 'altar', 'altas', 'altea', 'altos', 'aluda', 'alude', 
                              'aludi', 'aludo', 'aluga', 'alugo', 'aluga', 'aluna', 'aluno', 
                              'alvas', 'alves', 'alvor', 'alvos', 'alcai', 'alcam', 'alcar', 
                              'alcas', 'alcou', 'amada', 'amado', 'amais', 'amamo', 'amara', 
                              'amaro', 'amara', 'amava', 'ambas', 'ambos', 'ameba', 'ameia', 
                              'ameis', 'amemo', 'amena', 'ameno', 'ameca', 'amido', 'amiga', 
                              'amigo', 'amiga', 'amima', 'amime', 'amimo', 'amima', 'amola', 
                              'amole', 'amolo', 'amola', 'amora', 'ampla', 'amplo', 'anais', 
                              'ancas', 'ancia', 'andai', 'andam', 'andar', 'andas', 'andei', 
                              'andem', 'andes', 'andor', 'andou', 'andre', 'anela', 'anele', 
                              'anelo', 'anela', 'anexa', 'anexe', 'anexo', 'anexa', 'anglo', 
                              'angra', 'anima', 'anime', 'animo', 'anima', 'anjos', 'anota', 
                              'anote', 'anoto', 'anota', 'ansia', 'antas', 'antes', 'antro', 
                              'antao', 'anual', 'anuam', 'anuas', 'anuem', 'anuir', 'anuis', 
                              'anuiu', 'anula', 'anule', 'anulo', 'anula', 'anuia', 'anuis', 
                              'anzol', 'aneis', 'anoes', 'aonde', 'aorta', 'apaga', 'apago', 
                              'apaga', 'apara', 'apare', 'aparo', 'apara', 'apeai', 'apear', 
                              'apeei', 'apega', 'apego', 'apega', 'apeia', 'apeie', 'apeio', 
                              'apela', 'apele', 'apelo', 'apela', 'apena', 'apene', 'apeno', 
                              'apena', 'apeou', 'apita', 'apite', 'apito', 'apita', 'apoio', 
                              'apoia', 'apolo', 'aptas', 'aptos', 'apura', 'apure', 'apuro', 
                              'apura', 'apoia', 'apoie', 'apoio', 'aquem', 'arada', 'arado', 
                              'arais', 'arame', 'aramo', 'arara', 'arara', 'arava', 'araca', 
                              'arcai', 'arcam', 'arcar', 'arcas', 'arcos', 'arcou', 'ardam', 
                              'ardas', 'ardei', 'ardem', 'arder', 'ardes', 'ardeu', 'ardia', 
                              'ardil', 'ardis', 'ardor', 'areal', 'areia', 'areis', 'areja', 
                              'areje', 'arejo', 'areja', 'aremo', 'arena', 'arfai', 'arfam', 
                              'arfar', 'arfas', 'arfei', 'arfem', 'arfes', 'arfou', 'argua', 
                              'arguo', 'argui', 'argui', 'argui', 'armai', 'armam', 'armar', 
                              'armas', 'armei', 'armem', 'armes', 'armou', 'aroma', 'arpoa', 
                              'arpoe', 'arpoa', 'arpao', 'arpoo', 'arque', 'arrea', 'arria', 
                              'arrie', 'arrio', 'arria', 'arroz', 'artes', 'artur', 'asila', 
                              'asile', 'asilo', 'asila', 'asnos', 'aspas', 'assai', 'assam', 
                              'assar', 'assas', 'assaz', 'assei', 'assem', 'asses', 'assea', 
                              'assim', 'assis', 'assoa', 'assoe', 'assou', 'assoa', 'assoo', 
                              'astro', 'ataca', 'ataco', 'ataca', 'atada', 'atado', 'atais', 
                              'atamo', 'atara', 'atara', 'atava', 'ateai', 'atear', 'ateei', 
                              'ateia', 'ateie', 'ateio', 'ateis', 'atemo', 'ateou', 'atera', 
                              'ateus', 'ateve', 'atice', 'atido', 'atina', 'atine', 'atino', 
                              'atina', 'atira', 'atire', 'atiro', 'atira', 'ativa', 'ative', 
                              'ativo', 'ativa', 'atica', 'atico', 'atica', 'atlas', 'atola', 
                              'atole', 'atolo', 'atola', 'atrai', 'atrai', 'atriz', 'atras', 
                              'atuai', 'atual', 'atuam', 'atuar', 'atuas', 'atuei', 'atuem', 
                              'atues', 'atuns', 'atuou', 'atura', 'ature', 'aturo', 'atura', 
                              'ateia', 'atens', 'audaz', 'aulas', 'auras', 'autor', 'autos', 
                              'autua', 'autue', 'autuo', 'autua', 'avais', 'avara', 'avaro', 
                              'aveia', 'aveio', 'avela', 'aviai', 'aviam', 'aviar', 'avias', 
                              'aviei', 'aviem', 'avier', 'avies', 'avimo', 'aviou', 'avira', 
                              'avisa', 'avise', 'aviso', 'avisa', 'aviva', 'avive', 'avivo', 
                              'aviva', 'aviao', 'avens', 'axial', 'axila', 'azara', 'azare', 
                              'azaro', 'azara', 'azeda', 'azede', 'azedo', 'azeda', 'azias', 
                              'azoto', 'azuis', 'azula', 'azule', 'azulo', 'azula', 'acude', 
                              'acoes', 'aerea', 'aereo', 
                              'babai', 'babam', 'babar', 'babas', 'babei', 'babem', 'babes', 
                              'babou', 'babas', 'babao', 'bacia', 'bafos', 'bagas', 'bagos', 
                              'bahia', 'baias', 'baila', 'baile', 'bailo', 'baila', 'baita', 
                              'baixa', 'baixe', 'baixo', 'baixa', 'baiao', 'balam', 'balas', 
                              'balde', 'balem', 'bales', 'balea', 'balia', 'balir', 'balis', 
                              'baliu', 'balsa', 'balao', 'bamba', 'bambo', 'bambu', 'banal', 
                              'banca', 'banco', 'banca', 'banda', 'bando', 'banem', 'banes', 
                              'banha', 'banhe', 'banho', 'banha', 'bania', 'banir', 'banis', 
                              'baniu', 'banjo', 'baque', 'barba', 'barca', 'barco', 'bardo', 
                              'bares', 'barra', 'barre', 'barro', 'barra', 'barao', 'bases', 
                              'basea', 'basta', 'baste', 'basto', 'basta', 'batam', 'batas', 
                              'batei', 'batel', 'batem', 'bater', 'bates', 'bateu', 'batia', 
                              'batom', 'bauru', 'bazar', 'bacos', 'baias', 'beata', 'beato', 
                              'bebam', 'bebas', 'bebei', 'bebem', 'beber', 'bebes', 'bebeu', 
                              'bebia', 'bebes', 'becas', 'becos', 'beija', 'beije', 'beijo', 
                              'beija', 'beira', 'beire', 'beiro', 'beira', 'beico', 'belas', 
                              'belga', 'belos', 'bemol', 'benta', 'bento', 'benza', 'benze', 
                              'benzi', 'benzo', 'benze', 'beque', 'berna', 'berra', 'berre', 
                              'berro', 'berra', 'berco', 'besta', 'bicai', 'bicam', 'bicar', 
                              'bicas', 'bicha', 'bicho', 'bicos', 'bicou', 'biela', 'bigas', 
                              'bingo', 'bique', 'birra', 'bispo', 'bisao', 'blefa', 'blefe', 
                              'blefo', 'blefa', 'bloco', 'blusa', 'boate', 'boato', 'bobas', 
                              'bobea', 'bobos', 'bocal', 'bocas', 'bocha', 'bodas', 'bodes', 
                              'boiai', 'boiar', 'boiei', 'boina', 'boiou', 'bolai', 'bolam', 
                              'bolar', 'bolas', 'boldo', 'bolei', 'bolem', 'boles', 'bolha', 
                              'bolos', 'bolou', 'bolsa', 'bolso', 'bolao', 'bomba', 'bonde', 
                              'bones', 'borda', 'borde', 'bordo', 'borda', 'borra', 'borre', 
                              'borro', 'borra', 'bossa', 'bosta', 'botai', 'botam', 'botar', 
                              'botas', 'botei', 'botem', 'botes', 'botou', 'botao', 'boxea', 
                              'braba', 'brabo', 'brada', 'brade', 'brado', 'brada', 'braga', 
                              'brama', 'brame', 'brami', 'bramo', 'brama', 'brasa', 'brava', 
                              'bravo', 'braca', 'braco', 'breca', 'breco', 'breca', 'brejo', 
                              'breta', 'breve', 'breve', 'brida', 'briga', 'brigo', 'briga', 
                              'brins', 'brios', 'brisa', 'brita', 'brito', 'broas', 'broca', 
                              'broco', 'broca', 'bromo', 'brota', 'brote', 'broto', 'brota', 
                              'bruma', 'bruta', 'bruto', 'bruxa', 'bruxo', 'bucal', 'bucha', 
                              'bucho', 'bueno', 'bufai', 'bufam', 'bufar', 'bufas', 'bufei', 
                              'bufem', 'bufes', 'bufou', 'bufao', 'bujao', 'bulam', 'bulas', 
                              'bulbo', 'bules', 'bulia', 'bulir', 'bulis', 'buliu', 'bumbo', 
                              'bunda', 'bunde', 'bundo', 'bunda', 'burgo', 'burla', 'burle', 
                              'burlo', 'burla', 'burra', 'burro', 'busca', 'busco', 'busca', 
                              'busto', 'buxos', 'bario', 'bilis', 'boiam', 'boias', 'boiem', 
                              'boies', 'boers', 'bonus', 'buzio', 
                              'cabei', 'cabem', 'caber', 'cabes', 'cabia', 'cabos', 'cabra', 
                              'cacas', 'cacei', 'cacem', 'caces', 'cacho', 'cacos', 'cacto', 
                              'cafes', 'cagai', 'cagam', 'cagar', 'cagas', 'cagou', 'cague', 
                              'caiai', 'caiam', 'caiar', 'caias', 'caiba', 'caibo', 'caido', 
                              'caiei', 'caiem', 'caies', 'caiou', 'cairo', 'caira', 'caixa', 
                              'calai', 'calam', 'calar', 'calas', 'calca', 'calce', 'calco', 
                              'calca', 'calda', 'caldo', 'calei', 'calem', 'cales', 'calha', 
                              'calhe', 'calho', 'calha', 'calma', 'calmo', 'calor', 'calos', 
                              'calou', 'calva', 'calvo', 'calca', 'calco', 'calca', 'camas', 
                              'campo', 'canal', 'canas', 'canaa', 'canga', 'canja', 'canoa', 
                              'canos', 'cansa', 'canse', 'canso', 'cansa', 'canta', 'cante', 
                              'canto', 'canta', 'capai', 'capam', 'capar', 'capas', 'capaz', 
                              'capei', 'capem', 'capes', 'capim', 'capou', 'capta', 'capte', 
                              'capto', 'capta', 'caput', 'capuz', 'caras', 'cardo', 'carga', 
                              'cargo', 'carmo', 'carne', 'caros', 'carpa', 'carpe', 'carpi', 
                              'carro', 'carta', 'carao', 'casai', 'casal', 'casam', 'casar', 
                              'casas', 'casca', 'casco', 'casei', 'casem', 'cases', 'casos', 
                              'casou', 'caspa', 'cassa', 'casse', 'casso', 'cassa', 'casta', 
                              'casto', 'catai', 'catam', 'catar', 'catas', 'catei', 'catem', 
                              'cates', 'catou', 'catre', 'cauda', 'caule', 'causa', 'cause', 
                              'causo', 'causa', 'cauta', 'cauto', 'cavai', 'cavam', 'cavar', 
                              'cavas', 'cavei', 'cavem', 'caves', 'cavia', 'cavie', 'cavio', 
                              'cavia', 'cavou', 'cacai', 'cacam', 'cacar', 'cacas', 'cacoa', 
                              'cacoe', 'cacou', 'cacoa', 'cacao', 'cacoo', 'caiam', 'caias', 
                              'caida', 'caido', 'caimo', 'caira', 'ceado', 'ceais', 'ceamo', 
                              'ceara', 'ceara', 'ceava', 'cedam', 'cedas', 'cedei', 'cedem', 
                              'ceder', 'cedes', 'cedeu', 'cedia', 'cedro', 'ceeis', 'ceemo', 
                              'cegai', 'cegam', 'cegar', 'cegas', 'cegos', 'cegou', 'cegue', 
                              'ceiam', 'ceias', 'ceiem', 'ceies', 'ceifa', 'ceife', 'ceifo', 
                              'ceifa', 'celas', 'celta', 'cenas', 'censo', 'cento', 'ceras', 
                              'cerca', 'cerco', 'cerca', 'cerda', 'cerne', 'cerni', 'cerol', 
                              'cerra', 'cerre', 'cerro', 'cerra', 'certa', 'certo', 'cervo', 
                              'cessa', 'cesse', 'cesso', 'cessa', 'cesta', 'cesto', 'cetim', 
                              'cetro', 'chaga', 'chago', 'chaga', 'chale', 'chale', 'chama', 
                              'chame', 'chamo', 'chama', 'chapa', 'chata', 'chato', 'chave', 
                              'checa', 'checo', 'checa', 'chefa', 'chefe', 'chega', 'chego', 
                              'chega', 'cheia', 'cheio', 'chiai', 'chiam', 'chiar', 'chias', 
                              'chica', 'chico', 'chiei', 'chiem', 'chies', 'china', 'chiou', 
                              'choca', 'choco', 'choca', 'chora', 'chore', 'choro', 'chora', 
                              'chova', 'chove', 'chovi', 'chovo', 'chove', 'choca', 'chupa', 
                              'chupe', 'chupo', 'chupa', 'chuta', 'chute', 'chuto', 'chuta', 
                              'chuva', 'ciclo', 'cidra', 'cifra', 'cifre', 'cifro', 'cifra', 
                              'cinco', 'cinda', 'cinde', 'cindi', 'cindo', 'cinge', 'cingi', 
                              'cinja', 'cinjo', 'cinta', 'cinto', 'cinza', 'ciosa', 'cioso', 
                              'cipos', 'circo', 'cisca', 'cisco', 'cisca', 'cisma', 'cisme', 
                              'cismo', 'cisma', 'cisne', 'cisao', 'citai', 'citam', 'citar', 
                              'citas', 'citei', 'citem', 'cites', 'citou', 'civil', 'civis', 
                              'ciume', 'clama', 'clame', 'clamo', 'clama', 'clara', 'claro', 
                              'clava', 'clero', 'clima', 'clips', 'clone', 'cloro', 'clube', 
                              'coada', 'coado', 'coagi', 'coais', 'coaja', 'coajo', 'coamo', 
                              'coara', 'coara', 'coava', 'coaxa', 'coaxe', 'coaxo', 'coaxa', 
                              'cobra', 'cobre', 'cobri', 'cobro', 'cobra', 'cocal', 'cocei', 
                              'cocem', 'coces', 'cocho', 'cocos', 'coege', 'coeis', 'coemo', 
                              'coesa', 'coeso', 'coeva', 'coevo', 'cofre', 'coibi', 'coice', 
                              'coifa', 'coisa', 'coito', 'colai', 'colam', 'colar', 'colas', 
                              'colei', 'colem', 'coles', 'colha', 'colhe', 'colhi', 'colho', 
                              'colhe', 'colou', 'comam', 'comas', 'comei', 'comem', 'comer', 
                              'comes', 'comeu', 'comia', 'compo', 'comum', 'conde', 'cones', 
                              'conga', 'conta', 'conte', 'conto', 'conta', 'conte', 'copas', 
                              'copia', 'copie', 'copio', 'copia', 'copos', 'corai', 'coral', 
                              'coram', 'corar', 'coras', 'corda', 'corei', 'corem', 'cores', 
                              'corja', 'corno', 'coroa', 'coroe', 'coros', 'corou', 'coroa', 
                              'corpo', 'corra', 'corre', 'corri', 'corro', 'corre', 'corta', 
                              'corte', 'corto', 'corta', 'corvo', 'corca', 'coroa', 'coroo', 
                              'cosam', 'cosas', 'cosei', 'cosem', 'coser', 'coses', 'coseu', 
                              'cosia', 'cosmo', 'cospe', 'costa', 'cotai', 'cotam', 'cotar', 
                              'cotas', 'cotei', 'cotem', 'cotes', 'cotou', 'coube', 'couro', 
                              'couto', 'couve', 'covas', 'coxas', 'coxim', 'coxos', 'cozam', 
                              'cozas', 'cozei', 'cozem', 'cozer', 'cozes', 'cozeu', 'cozia', 
                              'cocai', 'cocam', 'cocar', 'cocas', 'cocou', 'coiba', 'coibe', 
                              'coibo', 'crava', 'crave', 'cravo', 'crava', 'crede', 'credo', 
                              'creia', 'creio', 'crema', 'creme', 'cremo', 'crema', 'crera', 
                              'crera', 'criai', 'criam', 'criar', 'crias', 'crido', 'criei', 
                              'criem', 'cries', 'crime', 'crina', 'criou', 'crise', 'criva', 
                              'crive', 'crivo', 'criva', 'croma', 'crome', 'cromo', 'croma', 
                              'cruas', 'cruel', 'cruza', 'cruze', 'cruzo', 'cruza', 'creem', 
                              'cubas', 'cubos', 'cubra', 'cubro', 'cucas', 'cucos', 'cueca', 
                              'cuias', 'cuida', 'cuide', 'cuido', 'cuida', 'cujas', 'cujos', 
                              'cujus', 'culpa', 'culpe', 'culpo', 'culpa', 'culta', 'culto', 
                              'cumes', 'cunha', 'cunhe', 'cunho', 'cunha', 'cupim', 'cupom', 
                              'curai', 'curam', 'curar', 'curas', 'curei', 'curem', 'cures', 
                              'curou', 'cursa', 'curse', 'curso', 'cursa', 'curta', 'curte', 
                              'curti', 'curto', 'curva', 'curve', 'curvo', 'curva', 'cuspa', 
                              'cuspi', 'cuspo', 'custa', 'custe', 'custo', 'custa', 'cuica', 
                              'capua', 'celia', 'cesar', 'cesio', 'cilio', 'cirio', 'civil', 
                              'colon', 'copia', 'codea', 'curia', 'cutis', 
                              'dadas', 'dados', 'damas', 'damos', 'danai', 'danam', 'danar', 
                              'danas', 'dance', 'dando', 'danei', 'danem', 'danes', 'danos', 
                              'danou', 'dante', 'danca', 'danco', 'danca', 'daqui', 'dardo', 
                              'darei', 'darem', 'dares', 'daria', 'daras', 'darao', 'datai', 
                              'datam', 'datar', 'datas', 'datei', 'datem', 'dates', 'datou', 
                              'davam', 'davas', 'decai', 'decai', 'dedal', 'dedos', 'deduz', 
                              'dedao', 'deita', 'deite', 'deito', 'deita', 'deixa', 'deixe', 
                              'deixo', 'deixa', 'delas', 'deles', 'delta', 'demos', 'demao', 
                              'densa', 'denso', 'dente', 'depor', 'depus', 'depos', 'depoe', 
                              'deram', 'deras', 'derem', 'deres', 'dermo', 'desce', 'desci', 
                              'desce', 'desde', 'despe', 'despi', 'dessa', 'desse', 'desta', 
                              'deste', 'desca', 'desco', 'deter', 'detem', 'deusa', 'devam', 
                              'devas', 'devei', 'devem', 'dever', 'deves', 'deveu', 'devia', 
                              'diabo', 'dicas', 'dieta', 'digam', 'digas', 'digna', 'digne', 
                              'digno', 'digna', 'dilua', 'dilui', 'diluo', 'dilui', 'diodo', 
                              'dique', 'direi', 'diria', 'diras', 'dirao', 'disca', 'disco', 
                              'disca', 'dispo', 'disse', 'disso', 'dista', 'diste', 'disto', 
                              'dista', 'ditai', 'ditam', 'ditar', 'ditas', 'ditei', 'ditem', 
                              'dites', 'ditos', 'ditou', 'divas', 'dizei', 'dizem', 'dizer', 
                              'dizes', 'dizia', 'doada', 'doado', 'doais', 'doamo', 'doara', 
                              'doara', 'doava', 'dobra', 'dobre', 'dobro', 'dobra', 'docas', 
                              'doeis', 'doemo', 'doera', 'doera', 'dogma', 'doida', 'doido', 
                              'domai', 'domam', 'domar', 'domas', 'domei', 'domem', 'domes', 
                              'domou', 'donas', 'donde', 'donos', 'dopai', 'dopam', 'dopar', 
                              'dopas', 'dopei', 'dopem', 'dopes', 'dopou', 'dores', 'dorme', 
                              'dormi', 'dorso', 'dosai', 'dosam', 'dosar', 'dosas', 'dosei', 
                              'dosem', 'doses', 'dosou', 'dotai', 'dotam', 'dotar', 'dotas', 
                              'dotei', 'dotem', 'dotes', 'dotou', 'doura', 'doure', 'douro', 
                              'doura', 'douta', 'douto', 'doiam', 'doias', 'doida', 'doido', 
                              'draga', 'drago', 'draga', 'drama', 'drena', 'drene', 'dreno', 
                              'drena', 'droga', 'drogo', 'droga', 'duais', 'dubla', 'duble', 
                              'dublo', 'dubla', 'ducha', 'duela', 'duele', 'duelo', 'duela', 
                              'dueto', 'dumas', 'dunas', 'dunga', 'dupla', 'duplo', 'duque', 
                              'durai', 'duram', 'durar', 'duras', 'durei', 'durem', 'dures', 
                              'durma', 'durmo', 'duros', 'durou', 'dutos', 'dalia', 'debil', 
                              'dolar', 'dubia', 'dubio', 'duzia', 
                              'ecoai', 'ecoam', 'ecoar', 'ecoas', 'ecoei', 'ecoem', 'ecoes', 
                              'ecoou', 'edema', 'edita', 'edite', 'edito', 'edita', 'educa', 
                              'educo', 'educa', 'egito', 'eiras', 'eixos', 'ejeta', 'ejete', 
                              'ejeto', 'ejeta', 'elege', 'elegi', 'elege', 'eleja', 'elejo', 
                              'eleva', 'eleve', 'elevo', 'eleva', 'elite', 'elixa', 'elixe', 
                              'elixi', 'elixo', 'elmos', 'emana', 'emane', 'emano', 'emana', 
                              'emita', 'emite', 'emiti', 'emito', 'emula', 'emule', 'emulo', 
                              'emula', 'encha', 'enche', 'enchi', 'encho', 'enche', 'enfia', 
                              'enfie', 'enfim', 'enfio', 'enfia', 'enjoa', 'enjoe', 'enjoa', 
                              'enjoo', 'enoja', 'enoje', 'enojo', 'enoja', 'entes', 'entoa', 
                              'entoe', 'entoa', 'entra', 'entre', 'entro', 'entra', 'entao', 
                              'entoo', 'envia', 'envie', 'envio', 'envia', 'ereta', 'ereto', 
                              'ergam', 'ergas', 'ergue', 'ergui', 'ergue', 'erice', 'erigi', 
                              'erija', 'erijo', 'erica', 'erico', 'erica', 'ermos', 'eroda', 
                              'erode', 'erodi', 'erodo', 'errai', 'erram', 'errar', 'erras', 
                              'errei', 'errem', 'erres', 'erros', 'errou', 'ervas', 'erige', 
                              'escoa', 'escoe', 'escol', 'escoa', 'escoo', 'espia', 'espie', 
                              'espio', 'espia', 'espia', 'esqui', 'essas', 'esses', 'estai', 
                              'estar', 'estas', 'estes', 'estio', 'estou', 'estas', 'estao', 
                              'esvai', 'esvai', 'etano', 'etapa', 'eteno', 'etilo', 'etnia', 
                              'etipe', 'evada', 'evade', 'evadi', 'evado', 'evita', 'evite', 
                              'evito', 'evita', 'evoca', 'evoco', 'evoca', 'exala', 'exale', 
                              'exalo', 'exala', 'exame', 'exara', 'exare', 'exaro', 'exara', 
                              'exata', 'exato', 'exiba', 'exibe', 'exibi', 'exibo', 'exige', 
                              'exigi', 'exija', 'exijo', 'exila', 'exile', 'exilo', 'exila', 
                              'exima', 'exime', 'eximi', 'eximo', 'expia', 'expie', 'expio', 
                              'expia', 'expor', 'expus', 'expos', 'expoe', 'extra', 'exuma', 
                              'exume', 'exumo', 'exuma', 
                              'facas', 'faces', 'facho', 'facao', 'fadas', 'fados', 'faina', 
                              'faixa', 'falai', 'falam', 'falar', 'falas', 'falda', 'falei', 
                              'falem', 'fales', 'falha', 'falhe', 'falho', 'falha', 'falia', 
                              'falir', 'falis', 'faliu', 'falou', 'falsa', 'falso', 'falta', 
                              'falte', 'falto', 'falta', 'famas', 'farda', 'fardo', 'farei', 
                              'faria', 'farol', 'faros', 'farpa', 'farra', 'farsa', 'farta', 
                              'farte', 'farto', 'farta', 'faras', 'farao', 'fases', 'fatal', 
                              'fatia', 'fatie', 'fatio', 'fatia', 'fator', 'fatos', 'fauna', 
                              'fauno', 'favas', 'favor', 'favos', 'fazei', 'fazem', 'fazer', 
                              'fazes', 'fazia', 'facam', 'facas', 'febre', 'fecal', 'fecha', 
                              'feche', 'fecho', 'fecha', 'fedam', 'fedas', 'fedei', 'fedem', 
                              'feder', 'fedes', 'fedeu', 'fedia', 'fedor', 'feias', 'feios', 
                              'feira', 'feita', 'feito', 'feixe', 'feliz', 'fenda', 'fende', 
                              'fendi', 'fendo', 'fende', 'feras', 'feraz', 'ferem', 'feres', 
                              'feria', 'ferir', 'feris', 'feriu', 'feroz', 'ferra', 'ferre', 
                              'ferro', 'ferra', 'ferva', 'ferve', 'fervi', 'fervo', 'ferve', 
                              'festa', 'fetal', 'fetos', 'feudo', 'fezes', 'fiado', 'fiais', 
                              'fiamo', 'fiapo', 'fiara', 'fiara', 'fiava', 'fibra', 'ficai', 
                              'ficam', 'ficar', 'ficas', 'ficha', 'fiche', 'ficho', 'ficha', 
                              'ficou', 'fieis', 'fiemo', 'figas', 'figos', 'filai', 'filam', 
                              'filar', 'filas', 'filei', 'filem', 'files', 'filha', 'filho', 
                              'filia', 'filie', 'filio', 'filia', 'filma', 'filme', 'filmo', 
                              'filma', 'filou', 'filao', 'final', 'finas', 'finca', 'finco', 
                              'finca', 'finda', 'finde', 'findo', 'finda', 'finge', 'fingi', 
                              'finja', 'finjo', 'finos', 'finta', 'finte', 'finto', 'finta', 
                              'fique', 'firam', 'firas', 'firma', 'firme', 'firmo', 'firma', 
                              'fisco', 'fisga', 'fisgo', 'fisga', 'fitai', 'fitam', 'fitar', 
                              'fitas', 'fitei', 'fitem', 'fites', 'fitou', 'fixai', 'fixam', 
                              'fixar', 'fixas', 'fixei', 'fixem', 'fixes', 'fixos', 'fixou', 
                              'fizer', 'fieis', 'flavo', 'floco', 'flora', 'flori', 'fluam', 
                              'fluas', 'fluem', 'fluir', 'fluis', 'fluiu', 'fluxo', 'fluia', 
                              'fluis', 'fobia', 'focai', 'focam', 'focar', 'focas', 'focos', 
                              'focou', 'fofas', 'fofos', 'fogem', 'foges', 'fogos', 'fogao', 
                              'foice', 'foles', 'folga', 'folgo', 'folga', 'folha', 'folia', 
                              'fomes', 'fomos', 'fones', 'fonte', 'foque', 'foram', 'foras', 
                              'forca', 'force', 'forem', 'fores', 'forja', 'forje', 'forjo', 
                              'forja', 'forma', 'forme', 'formo', 'forma', 'forno', 'foros', 
                              'forra', 'forre', 'forro', 'forra', 'forte', 'forca', 'forco', 
                              'forca', 'fosca', 'fosco', 'fossa', 'fosse', 'fosso', 'foste', 
                              'fotos', 'fraca', 'fraco', 'frade', 'fraga', 'frase', 'freai', 
                              'frear', 'freei', 'freia', 'freie', 'freio', 'freme', 'fremi', 
                              'freou', 'fresa', 'frese', 'freso', 'fresa', 'freta', 'frete', 
                              'freto', 'freta', 'frevo', 'frias', 'frigi', 'frija', 'frijo', 
                              'frios', 'frisa', 'frise', 'friso', 'frisa', 'frita', 'frite', 
                              'frito', 'frita', 'frota', 'fruam', 'fruas', 'fruem', 'fruir', 
                              'fruis', 'fruiu', 'fruta', 'fruto', 'fruia', 'fruis', 'frige', 
                              'fucei', 'fucem', 'fuces', 'fugas', 'fugaz', 'fugia', 'fugir', 
                              'fugis', 'fugiu', 'fujam', 'fujas', 'fujem', 'fujes', 'fujia', 
                              'fujir', 'fujis', 'fujiu', 'fujao', 'fulge', 'fulgi', 'fumai', 
                              'fumam', 'fumar', 'fumas', 'fumei', 'fumem', 'fumes', 'fumou', 
                              'funda', 'funde', 'fundi', 'fundo', 'funda', 'funga', 'fungo', 
                              'funga', 'funil', 'funis', 'furai', 'furam', 'furar', 'furas', 
                              'furei', 'furem', 'fures', 'furna', 'furor', 'furos', 'furou', 
                              'furta', 'furte', 'furto', 'furta', 'furao', 'fusco', 'fusos', 
                              'fusao', 'fuzil', 'fuzis', 'fucai', 'fucam', 'fucar', 'fucas', 
                              'fucou', 'facil', 'fatuo', 'felix', 'feria', 'femea', 'femur', 
                              'forum', 'forca', 'furia', 'futil', 
                              'gabai', 'gabam', 'gabar', 'gabas', 'gabei', 'gabem', 'gabes', 
                              'gabou', 'gados', 'gagas', 'gagos', 'gaita', 'gajas', 'gajos', 
                              'galas', 'galga', 'galgo', 'galga', 'galho', 'galos', 'galao', 
                              'gamba', 'gamos', 'gamao', 'ganem', 'ganes', 'ganha', 'ganhe', 
                              'ganho', 'ganha', 'gania', 'ganir', 'ganis', 'ganiu', 'ganso', 
                              'garbo', 'garfa', 'garfe', 'garfo', 'garfa', 'garis', 'garoa', 
                              'garoe', 'garoa', 'garra', 'garca', 'garoa', 'garoo', 'gases', 
                              'gasta', 'gaste', 'gasto', 'gasta', 'gatas', 'gatos', 'gazua', 
                              'geada', 'geado', 'geais', 'geamo', 'geara', 'geara', 'geava', 
                              'geeis', 'geemo', 'geiam', 'geias', 'geiem', 'geies', 'gelai', 
                              'gelam', 'gelar', 'gelas', 'gelei', 'gelem', 'geles', 'gelos', 
                              'gelou', 'gemam', 'gemas', 'gemei', 'gemem', 'gemer', 'gemes', 
                              'gemeu', 'gemia', 'genes', 'genro', 'gente', 'gerai', 'geral', 
                              'geram', 'gerar', 'geras', 'gerei', 'gerem', 'geres', 'geria', 
                              'gerir', 'geris', 'geriu', 'germe', 'gerou', 'gesso', 'gesta', 
                              'gesto', 'gibao', 'ginga', 'gingo', 'ginga', 'girai', 'giram', 
                              'girar', 'giras', 'girei', 'girem', 'gires', 'giros', 'girou', 
                              'gleba', 'globo', 'glosa', 'glose', 'gloso', 'glosa', 'gnomo', 
                              'goela', 'goias', 'golas', 'goles', 'golea', 'golfo', 'golpe', 
                              'gomas', 'gomes', 'gomos', 'gongo', 'gonzo', 'gorai', 'goram', 
                              'gorar', 'goras', 'gorda', 'gordo', 'gorei', 'gorem', 'gores', 
                              'gorou', 'gorro', 'gosma', 'gosta', 'goste', 'gosto', 'gosta', 
                              'gotas', 'gozai', 'gozam', 'gozar', 'gozas', 'gozei', 'gozem', 
                              'gozes', 'gozos', 'gozou', 'grade', 'grafa', 'grafe', 'grafo', 
                              'grafa', 'grama', 'grana', 'grata', 'grato', 'graus', 'grava', 
                              'grave', 'gravo', 'grava', 'graxa', 'graxo', 'graca', 'grega', 
                              'grego', 'greve', 'grifa', 'grife', 'grifo', 'grifa', 'grila', 
                              'grile', 'grilo', 'grila', 'gripe', 'grita', 'grite', 'grito', 
                              'grita', 'gruda', 'grude', 'grudo', 'gruda', 'grupo', 'gruta', 
                              'graos', 'gueto', 'guiai', 'guiam', 'guiar', 'guias', 'guiei', 
                              'guiem', 'guies', 'guiou', 'guisa', 'guizo', 'gumes', 'guria', 
                              'guris', 'galia', 'gemea', 'gemeo', 'genio', 'giria', 'godos', 
                              'hajam', 'hajas', 'halos', 'haras', 'harpa', 'harem', 'haste', 
                              'haure', 'hauri', 'havei', 'haver', 'havia', 'heras', 'herda', 
                              'herde', 'herdo', 'herda', 'heroi', 'hiato', 'hiena', 'hindu', 
                              'hinos', 'homem', 'honra', 'honre', 'honro', 'honra', 'horas', 
                              'horda', 'horta', 'horto', 'hotel', 'houve', 'hulha', 'humor', 
                              'hunos', 'hurra', 'habil', 'helio', 'hifen', 'himen', 'humus', 
                              'iates', 'ibero', 'iceis', 'icemo', 'idade', 'ideal', 'idosa', 
                              'idoso', 'ideia', 'ienes', 'igapo', 'igual', 'ilesa', 'ileso', 
                              'ilhai', 'ilham', 'ilhar', 'ilhas', 'ilhei', 'ilhem', 'ilhes', 
                              'ilhou', 'iluda', 'ilude', 'iludi', 'iludo', 'imita', 'imite', 
                              'imito', 'imita', 'imola', 'imole', 'imolo', 'imola', 'impor', 
                              'impus', 'impos', 'impoe', 'imune', 'inala', 'inale', 'inalo', 
                              'inala', 'inata', 'inato', 'incas', 'incha', 'inche', 'incho', 
                              'incha', 'incoa', 'incoe', 'incoa', 'incoo', 'induz', 'infla', 
                              'infle', 'inflo', 'infla', 'infra', 'iniba', 'inibe', 'inibi', 
                              'inibo', 'inova', 'inove', 'inovo', 'inova', 'insta', 'inste', 
                              'insto', 'insta', 'inter', 'intua', 'intui', 'intuo', 'intui', 
                              'inves', 'irada', 'irado', 'irdes', 'ireis', 'iremo', 'iriam', 
                              'irias', 'irmos', 'irmao', 'irmas', 'iscas', 'isola', 'isole', 
                              'isolo', 'isola', 'istmo', 'itera', 'itere', 'itero', 'itera', 
                              'icada', 'icado', 'icais', 'icamo', 'icara', 'icara', 'icava', 
                              'jacas', 'janta', 'jante', 'janto', 'janta', 'japao', 'jarda', 
                              'jarra', 'jarro', 'jatos', 'jaula', 'jazam', 'jazas', 'jazei', 
                              'jazem', 'jazer', 'jazes', 'jazeu', 'jazia', 'jecas', 'jegue', 
                              'jeito', 'jejua', 'jejue', 'jejum', 'jejuo', 'jejua', 'jesus', 
                              'jinga', 'joana', 'jogai', 'jogam', 'jogar', 'jogas', 'jogos', 
                              'jogou', 'jogue', 'jorge', 'jorra', 'jorre', 'jorro', 'jorra', 
                              'jovem', 'jubas', 'judas', 'judeu', 'judia', 'judie', 'judio', 
                              'judia', 'julga', 'julgo', 'julga', 'julho', 'junco', 'junho', 
                              'junta', 'junte', 'junto', 'junta', 'jurai', 'juram', 'jurar', 
                              'juras', 'jurei', 'jurem', 'jures', 'juros', 'jurou', 'justa', 
                              'justo', 'juiza', 'juizo', 'joias', 
                              'labor', 'lacei', 'lacem', 'laces', 'lacra', 'lacre', 'lacro', 
                              'lacra', 'lados', 'ladra', 'ladre', 'ladro', 'ladra', 'lagar', 
                              'lagoa', 'lagos', 'laica', 'laico', 'lajes', 'lamba', 'lambe', 
                              'lambi', 'lambo', 'lambe', 'lance', 'lanca', 'lanco', 'lanca', 
                              'lapso', 'lares', 'larga', 'largo', 'larga', 'larva', 'lasca', 
                              'lasco', 'lasca', 'laser', 'latas', 'latem', 'lates', 'latia', 
                              'latim', 'latir', 'latis', 'latiu', 'latao', 'lauda', 'laudo', 
                              'lavai', 'lavam', 'lavar', 'lavas', 'lavei', 'lavem', 'laves', 
                              'lavou', 'lavra', 'lavre', 'lavro', 'lavra', 'lazer', 'lacai', 
                              'lacam', 'lacar', 'lacas', 'lacos', 'lacou', 'leais', 'lebre', 
                              'ledes', 'legai', 'legal', 'legam', 'legar', 'legas', 'legou', 
                              'legue', 'leiam', 'leias', 'leiga', 'leigo', 'leite', 'leito', 
                              'lemas', 'lemes', 'lemos', 'lenda', 'lendo', 'lenga', 'lenha', 
                              'lenho', 'lenta', 'lente', 'lento', 'lenco', 'leoas', 'lepra', 
                              'leque', 'leram', 'leras', 'lerda', 'lerdo', 'lerei', 'lerem', 
                              'leres', 'leria', 'lermo', 'leras', 'lerao', 'lesai', 'lesam', 
                              'lesar', 'lesas', 'lesei', 'lesem', 'leses', 'lesma', 'lesou', 
                              'lesse', 'leste', 'lesao', 'letra', 'levai', 'levam', 'levar', 
                              'levas', 'levei', 'levem', 'leves', 'levou', 'leoes', 'lhama', 
                              'liame', 'libra', 'liceu', 'licor', 'lidai', 'lidam', 'lidar', 
                              'lidas', 'lidei', 'lidem', 'lides', 'lidos', 'lidou', 'ligai', 
                              'ligam', 'ligar', 'ligas', 'ligou', 'ligue', 'lilas', 'limai', 
                              'limam', 'limar', 'limas', 'limbo', 'limei', 'limem', 'limes', 
                              'limou', 'limpa', 'limpe', 'limpo', 'limpa', 'limao', 'lince', 
                              'linda', 'lindo', 'linfa', 'linha', 'linho', 'liras', 'lisas', 
                              'lisos', 'lista', 'liste', 'listo', 'lista', 'litro', 'livra', 
                              'livre', 'livro', 'livra', 'lixai', 'lixam', 'lixar', 'lixas', 
                              'lixei', 'lixem', 'lixes', 'lixou', 'lixao', 'licao', 'lobas', 
                              'lobos', 'lobao', 'locai', 'local', 'locam', 'locar', 'locas', 
                              'locou', 'logra', 'logre', 'logro', 'logra', 'loira', 'loiro', 
                              'lojas', 'lombo', 'lonas', 'longa', 'longe', 'longo', 'lopes', 
                              'loque', 'lorde', 'lotai', 'lotam', 'lotar', 'lotas', 'lotei', 
                              'lotem', 'lotes', 'lotea', 'lotou', 'louca', 'louco', 'loura', 
                              'louro', 'lousa', 'louva', 'louve', 'louvo', 'louva', 'louca', 
                              'louca', 'locao', 'lucas', 'lucra', 'lucre', 'lucro', 'lucra', 
                              'lugar', 'lulas', 'lunar', 'lupas', 'lusas', 'lusos', 'lutai', 
                              'lutam', 'lutar', 'lutas', 'lutei', 'lutem', 'lutes', 'lutou', 
                              'luvas', 'luxos', 'luzam', 'luzas', 'luzem', 'luzes', 'luzia', 
                              'luzir', 'luzis', 'luziu', 'labia', 'labio', 'lacio', 'lapis', 
                              'latex', 'legua', 'lider', 'lieis', 'lirio', 'litio', 'lotus', 
                              'macas', 'macho', 'macia', 'macio', 'macro', 'magia', 'magma', 
                              'magna', 'magno', 'magoa', 'magoe', 'magos', 'magoa', 'magra', 
                              'magro', 'magoo', 'maias', 'maior', 'major', 'malas', 'males', 
                              'malha', 'malhe', 'malho', 'malha', 'malta', 'mamai', 'mamam', 
                              'mamar', 'mamas', 'mamei', 'mamem', 'mames', 'mamou', 'mamae', 
                              'mamao', 'manas', 'manca', 'manco', 'manca', 'manda', 'mande', 
                              'mando', 'manda', 'manea', 'manga', 'manha', 'manha', 'mania', 
                              'manja', 'manje', 'manjo', 'manja', 'manos', 'mansa', 'manso', 
                              'manta', 'manto', 'mante', 'manes', 'mapas', 'mapea', 'marca', 
                              'marco', 'marca', 'mares', 'maria', 'marra', 'marta', 'marco', 
                              'mares', 'masca', 'masco', 'masca', 'massa', 'matai', 'matam', 
                              'matar', 'matas', 'matei', 'matem', 'mates', 'matiz', 'matos', 
                              'matou', 'macas', 'macom', 'macos', 'macas', 'meada', 'mecha', 
                              'medem', 'medes', 'media', 'medir', 'medis', 'mediu', 'media', 
                              'medos', 'medra', 'medre', 'medro', 'medra', 'meias', 'meiga', 
                              'meigo', 'meios', 'meiao', 'melai', 'melam', 'melar', 'melas', 
                              'melei', 'melem', 'meles', 'melou', 'melro', 'melao', 'menea', 
                              'menir', 'menor', 'menos', 'menta', 'mente', 'menti', 'menus', 
                              'meras', 'merce', 'merda', 'meros', 'mesas', 'meses', 'mesma', 
                              'mesmo', 'metal', 'metam', 'metas', 'metei', 'metem', 'meter', 
                              'metes', 'meteu', 'metia', 'metro', 'mexam', 'mexas', 'mexei', 
                              'mexem', 'mexer', 'mexes', 'mexeu', 'mexia', 'mecam', 'mecas', 
                              'miado', 'miais', 'miamo', 'miara', 'miara', 'miava', 'micos', 
                              'micro', 'mieis', 'miemo', 'migra', 'migre', 'migro', 'migra', 
                              'mijai', 'mijam', 'mijar', 'mijas', 'mijei', 'mijem', 'mijes', 
                              'mijou', 'milha', 'milho', 'mimai', 'mimam', 'mimar', 'mimas', 
                              'mimei', 'mimem', 'mimes', 'mimos', 'mimou', 'minai', 'minam', 
                              'minar', 'minas', 'minei', 'minem', 'mines', 'minha', 'minis', 
                              'minou', 'minta', 'minto', 'miolo', 'mirai', 'miram', 'mirar', 
                              'miras', 'mirei', 'mirem', 'mires', 'mirou', 'mirra', 'missa', 
                              'mista', 'misto', 'mitos', 'mitra', 'mixos', 'mixto', 'miuda', 
                              'miudo', 'moais', 'moamo', 'modas', 'modem', 'modos', 'moeda', 
                              'moeis', 'moela', 'moemo', 'moera', 'moera', 'mofai', 'mofam', 
                              'mofar', 'mofas', 'mofei', 'mofem', 'mofes', 'mofou', 'mogem', 
                              'moges', 'mogno', 'mogol', 'moita', 'molar', 'molas', 'molda', 
                              'molde', 'moldo', 'molda', 'moles', 'molha', 'molhe', 'molho', 
                              'molha', 'momos', 'monge', 'monja', 'monta', 'monte', 'monto', 
                              'monta', 'morai', 'moral', 'moram', 'morar', 'moras', 'morda', 
                              'morde', 'mordi', 'mordo', 'morde', 'morei', 'morem', 'mores', 
                              'morna', 'morno', 'morou', 'morra', 'morre', 'morri', 'morro', 
                              'morre', 'morsa', 'morse', 'morta', 'morte', 'morto', 'mosca', 
                              'mosca', 'motel', 'motor', 'motos', 'moura', 'mouro', 'movam', 
                              'movas', 'movei', 'movem', 'mover', 'moves', 'moveu', 'movia', 
                              'mocas', 'mocos', 'mocao', 'moiam', 'moias', 'moida', 'moido', 
                              'mucos', 'mudai', 'mudam', 'mudar', 'mudas', 'mudei', 'mudem', 
                              'mudes', 'mudez', 'mudos', 'mudou', 'mugia', 'mugir', 'mugis', 
                              'mugiu', 'muita', 'muito', 'mujam', 'mujas', 'mulas', 'multa',
                              'multe', 'multi', 'multo', 'multa', 'mundo', 'munem', 'munes', 
                              'munia', 'munir', 'munis', 'muniu', 'murai', 'mural', 'muram', 
                              'murar', 'muras', 'murei', 'murem', 'mures', 'muros', 'murou', 
                              'murro', 'musas', 'musca', 'musco', 'museu', 'musgo', 'mafia', 
                              'magoa', 'mario', 'media', 'medio', 'midia', 'miope', 'movel', 
                              'mumia', 'mutua', 'mutuo', 
                              'nabla', 'nabos', 'nacos', 'nadai', 'nadam', 'nadar', 'nadas', 
                              'nadei', 'nadem', 'nades', 'nadou', 'nafta', 'naipe', 'nanai', 
                              'nanam', 'nanar', 'nanas', 'nanei', 'nanem', 'nanes', 'nanou', 
                              'nardo', 'nariz', 'narra', 'narre', 'narro', 'narra', 'nasal', 
                              'nasce', 'nasci', 'nasce', 'nasca', 'nasco', 'natal', 'natas', 
                              'natos', 'nauta', 'naval', 'naves', 'navio', 'nacao', 'negai', 
                              'negam', 'negar', 'negas', 'negou', 'negra', 'negro', 'negue', 
                              'negao', 'nelas', 'neles', 'nenem', 'nenes', 'nervo', 'nesga', 
                              'nessa', 'nesse', 'nesta', 'neste', 'netas', 'netos', 'nevai', 
                              'nevam', 'nevar', 'nevas', 'nevei', 'nevem', 'neves', 'nevou', 
                              'nexos', 'nicho', 'ninai', 'ninam', 'ninar', 'ninas', 'ninei', 
                              'ninem', 'nines', 'ninfa', 'ninho', 'ninou', 'nisso', 'nisto', 
                              'nitro', 'nobre', 'nodal', 'noite', 'noiva', 'noive', 'noivo', 
                              'noiva', 'nomes', 'nomea', 'noras', 'norma', 'norte', 'nossa', 
                              'nosso', 'notai', 'notam', 'notar', 'notas', 'notei', 'notem', 
                              'notes', 'notou', 'novas', 'novos', 'nozes', 'nocao', 'nudez', 
                              'nulas', 'nulos', 'numas', 'nunca', 'nunes', 'nutra', 'nutre', 
                              'nutri', 'nutro', 'nuvem', 'nevoa', 'nivel', 'nodoa', 
                              'obesa', 'obeso', 'obras', 'obsta', 'obste', 'obsto', 'obsta', 
                              'obter', 'obtem', 'obvia', 'obvie', 'obvio', 'obvia', 'ocaso', 
                              'ocupa', 'ocupe', 'ocupo', 'ocupa', 'odeia', 'odeie', 'odeio', 
                              'odiai', 'odiar', 'odiei', 'odiou', 'oeste', 'ogiva', 'oitao', 
                              'olhai', 'olham', 'olhar', 'olhas', 'olhei', 'olhem', 'olhes', 
                              'olhos', 'olhou', 'oliva', 'ombro', 'omega', 'omita', 'omite', 
                              'omiti', 'omito', 'ondas', 'ondea', 'onera', 'onere', 'onero', 
                              'onera', 'ontem', 'oncas', 'opaca', 'opaco', 'opala', 'opera', 
                              'opere', 'opero', 'opera', 'opina', 'opine', 'opino', 'opina', 
                              'opomo', 'opora', 'optai', 'optam', 'optar', 'optas', 'optei', 
                              'optem', 'optes', 'optou', 'opcao', 'opoem', 'opoes', 'orado', 
                              'orais', 'oramo', 'orara', 'orara', 'orava', 'orcas', 'orcei', 
                              'orcem', 'orces', 'ordem', 'oreis', 'oremo', 'orgem', 'orges', 
                              'orgia', 'orlai', 'orlam', 'orlar', 'orlas', 'orlei', 'orlem', 
                              'orles', 'orlou', 'ornai', 'ornam', 'ornar', 'ornas', 'ornei', 
                              'ornem', 'ornes', 'ornou', 'orcai', 'orcam', 'orcar', 'orcas', 
                              'orcou', 'ossos', 'ostra', 'ouros', 'ousai', 'ousam', 'ousar', 
                              'ousas', 'ousei', 'ousem', 'ouses', 'ousou', 'outra', 'outro', 
                              'ouvem', 'ouves', 'ouvia', 'ouvir', 'ouvis', 'ouviu', 'oucam', 
                              'oucas', 'ovais', 'ovino', 'oxala', 'oxida', 'oxide', 'oxido', 
                              'oxida', 'oasis', 
                              'pacto', 'padre', 'pagai', 'pagam', 'pagar', 'pagas', 'pagem', 
                              'pagos', 'pagou', 'pague', 'pagao', 'pagas', 'paira', 'paire', 
                              'pairo', 'paira', 'pajea', 'palco', 'palha', 'palma', 'palmo', 
                              'pampa', 'panca', 'panda', 'panos', 'panca', 'papai', 'papam', 
                              'papar', 'papas', 'papei', 'papel', 'papem', 'papes', 'papos', 
                              'papou', 'papao', 'parai', 'param', 'parar', 'paras', 'parca', 
                              'parco', 'parda', 'pardo', 'parei', 'parem', 'pares', 'parea', 
                              'paria', 'parir', 'paris', 'pariu', 'parou', 'parta', 'parte', 
                              'parti', 'parto', 'parvo', 'pasma', 'pasme', 'pasmo', 'pasma', 
                              'passa', 'passe', 'passo', 'passa', 'pasta', 'paste', 'pasto', 
                              'pasta', 'patas', 'patim', 'patos', 'patua', 'paula', 'paulo', 
                              'pausa', 'pauta', 'paute', 'pauto', 'pauta', 'pavio', 'pavor', 
                              'pavao', 'pazes', 'pecai', 'pecam', 'pecar', 'pecas', 'pecou', 
                              'pedal', 'pedem', 'pedes', 'pedia', 'pedir', 'pedis', 'pediu', 
                              'pedra', 'pedro', 'pegai', 'pegam', 'pegar', 'pegas', 'pegou', 
                              'pegue', 'peida', 'peide', 'peido', 'peida', 'peita', 'peite', 
                              'peito', 'peita', 'peixe', 'pelai', 'pelam', 'pelar', 'pelas', 
                              'pelei', 'pelem', 'peles', 'pelos', 'pelou', 'penai', 'penal', 
                              'penam', 'penar', 'penas', 'penca', 'penda', 'pende', 'pendi', 
                              'pendo', 'pende', 'penei', 'penem', 'penes', 'penou', 'pensa', 
                              'pense', 'penso', 'pensa', 'pente', 'peque', 'peras', 'perca', 
                              'perco', 'perda', 'perde', 'perdi', 'perde', 'perna', 'persa', 
                              'perto', 'perua', 'perus', 'pesai', 'pesam', 'pesar', 'pesas', 
                              'pesca', 'pesco', 'pesca', 'pesei', 'pesem', 'peses', 'pesos', 
                              'pesou', 'peste', 'petiz', 'pecam', 'pecas', 'peoes', 'piada', 
                              'piado', 'piais', 'piamo', 'piano', 'piara', 'piara', 'piaui', 
                              'piava', 'picai', 'picam', 'picar', 'picas', 'picha', 'piche', 
                              'picho', 'picha', 'picos', 'picou', 'picao', 'pieis', 'piemo', 
                              'pifai', 'pifam', 'pifar', 'pifas', 'pifei', 'pifem', 'pifes', 
                              'pifou', 'pilar', 'pilha', 'pilhe', 'pilho', 'pilha', 'pilao', 
                              'pince', 'pinga', 'pingo', 'pinga', 'pinha', 'pinho', 'pinos', 
                              'pinta', 'pinte', 'pinto', 'pinta', 'pinca', 'pinco', 'pinca', 
                              'piora', 'piore', 'pioro', 'piora', 'pipas', 'pique', 'pires', 
                              'pirao', 'pisai', 'pisam', 'pisar', 'pisas', 'pisca', 'pisco', 
                              'pisca', 'pisei', 'pisem', 'pises', 'pisou', 'pista', 'pivos', 
                              'pixel', 'pizza', 'placa', 'plana', 'plane', 'plano', 'plana', 
                              'plato', 'plebe', 'plena', 'pleno', 'plota', 'plote', 'ploto', 
                              'plota', 'pluga', 'plugo', 'pluga', 'pluma', 'pneus', 'pobre', 
                              'podai', 'podam', 'podar', 'podas', 'podei', 'podem', 'poder', 
                              'podes', 'podia', 'podou', 'poema', 'poeta', 'polar', 'polca', 
                              'polia', 'polir', 'polis', 'poliu', 'polpa', 'polvo', 'pomar', 
                              'pomba', 'pombo', 'pomos', 'pompa', 'ponca', 'ponde', 'pondo', 
                              'ponha', 'ponho', 'ponta', 'ponte', 'ponto', 'porca', 'porco', 
                              'porei', 'porem', 'pores', 'poria', 'poros', 'porra', 'porre', 
                              'porta', 'porte', 'porto', 'porta', 'poras', 'porao', 'porem', 
                              'posai', 'posam', 'posar', 'posas', 'posei', 'posem', 'poses', 
                              'posou', 'pospo', 'possa', 'posse', 'posso', 'posta', 'poste', 
                              'posto', 'posta', 'potes', 'potro', 'pouca', 'pouco', 'poupa', 
                              'poupe', 'poupo', 'poupa', 'pousa', 'pouse', 'pouso', 'pousa', 
                              'povoa', 'povoe', 'povos', 'povoa', 'povao', 'povoo', 'pocas', 
                              'pocos', 'pocao', 'prado', 'praga', 'praia', 'prata', 'prato', 
                              'praxe', 'prazo', 'praca', 'prece', 'prega', 'prego', 'prega', 
                              'prelo', 'prema', 'preme', 'premi', 'premo', 'prepo', 'presa', 
                              'preso', 'preta', 'preto', 'previ', 'preve', 'preza', 'preze', 
                              'prezo', 'preza', 'preco', 'prima', 'prime', 'primo', 'prima', 
                              'priva', 'prive', 'privo', 'priva', 'proas', 'prole', 'propo', 
                              'prosa', 'prova', 'prove', 'provi', 'provo', 'prova', 'prove', 
                              'prumo', 'puder', 'pudim', 'pudor', 'pulai', 'pulam', 'pular', 
                              'pulas', 'pulei', 'pulem', 'pules', 'pulga', 'pulos', 'pulou', 
                              'pulsa', 'pulse', 'pulso', 'pulsa', 'pumas', 'punam', 'punas', 
                              'punem', 'punes', 'punha', 'punho', 'punia', 'punir', 'punis', 
                              'puniu', 'puras', 'purga', 'purgo', 'purga', 'puros', 'puser', 
                              'putas', 'putos', 'puxai', 'puxam', 'puxar', 'puxas', 'puxei', 
                              'puxem', 'puxes', 'puxou', 'puxao', 'pareo', 'patio', 'pelos', 
                              'penis', 'podio', 'polos', 'ponei', 'pubis', 
                              'quais', 'quase', 'queda', 'quede', 'quedo', 'queda', 'quepe', 
                              'quero', 'quere', 'quilo', 'quina', 'quipa', 'quita', 'quite', 
                              'quito', 'quita', 'quica', 'quota', 
                              'rabos', 'racha', 'rache', 'racho', 'racha', 'radar', 'radia', 
                              'radie', 'radio', 'radia', 'raiai', 'raiam', 'raiar', 'raias', 
                              'raiei', 'raiem', 'raies', 'raios', 'raiou', 'raiva', 'rajai', 
                              'rajam', 'rajar', 'rajas', 'rajei', 'rajem', 'rajes', 'rajou', 
                              'ralai', 'ralam', 'ralar', 'ralas', 'ralei', 'ralem', 'rales', 
                              'ralha', 'ralhe', 'ralho', 'ralha', 'ralos', 'ralou', 'ramos', 
                              'rampa', 'range', 'rangi', 'range', 'ranja', 'ranjo', 'ranco', 
                              'rapai', 'rapam', 'rapar', 'rapas', 'rapaz', 'rapei', 'rapem', 
                              'rapes', 'rapou', 'rapta', 'rapte', 'rapto', 'rapta', 'rapes', 
                              'raras', 'rarea', 'raros', 'rasas', 'rasga', 'rasgo', 'rasga', 
                              'rasos', 'raspa', 'raspe', 'raspo', 'raspa', 'rasto', 'ratas', 
                              'ratea', 'ratos', 'razao', 'racas', 'racao', 'reagi', 'reais', 
                              'reaja', 'reajo', 'reata', 'reate', 'reato', 'reata', 'reave', 
                              'reboa', 'reboe', 'reboa', 'reboo', 'recai', 'recai', 'recea', 
                              'recua', 'recue', 'recuo', 'recua', 'recem', 'redes', 'redil', 
                              'redor', 'reduz', 'reege', 'refaz', 'refez', 'refiz', 'refem', 
                              'regai', 'regam', 'regar', 'regas', 'regei', 'regem', 'reger', 
                              'reges', 'regeu', 'regia', 'regou', 'regra', 'regre', 'regro', 
                              'regra', 'regue', 'reina', 'reine', 'reino', 'reina', 'rejam', 
                              'rejas', 'reler', 'reles', 'releu', 'relia', 'relva', 'reles', 
                              'remai', 'remam', 'remar', 'remas', 'remei', 'remem', 'remes', 
                              'remia', 'remir', 'remis', 'remiu', 'remoa', 'remoe', 'remos', 
                              'remou', 'remoe', 'remoi', 'remoi', 'remoo', 'renal', 'renas', 
                              'renda', 'rende', 'rendi', 'rendo', 'rende', 'rente', 'repor', 
                              'repus', 'repos', 'repoe', 'reses', 'resma', 'resta', 'reste', 
                              'resto', 'resta', 'retas', 'reter', 'retos', 'retem', 'reuni', 
                              'rever', 'revia', 'revir', 'reviu', 'reves', 'reves', 'rezai', 
                              'rezam', 'rezar', 'rezas', 'rezei', 'rezem', 'rezes', 'rezou', 
                              'reuna', 'reune', 'reuno', 'riais', 'riamo', 'ribas', 'ricas', 
                              'ricos', 'rides', 'rifai', 'rifam', 'rifar', 'rifas', 'rifei', 
                              'rifem', 'rifes', 'rifle', 'rifou', 'rigor', 'rijas', 'rijos', 
                              'rimai', 'rimam', 'rimar', 'rimas', 'rimei', 'rimem', 'rimes', 
                              'rimos', 'rimou', 'rindo', 'ripas', 'riram', 'riras', 'rirei', 
                              'rirem', 'rires', 'riria', 'rirmo', 'riras', 'rirao', 'risca', 
                              'risco', 'risca', 'risos', 'risse', 'riste', 'ritmo', 'ritos', 
                              'rival', 'rixas', 'roais', 'roamo', 'robos', 'rocas', 'rocei', 
                              'rocem', 'roces', 'rocha', 'rodai', 'rodam', 'rodar', 'rodas', 
                              'rodei', 'rodem', 'rodes', 'rodea', 'rodos', 'rodou', 'roeis', 
                              'roemo', 'roera', 'roera', 'rogai', 'rogam', 'rogar', 'rogas', 
                              'rogem', 'roges', 'rogos', 'rogou', 'rogue', 'rojao', 'rolai', 
                              'rolam', 'rolar', 'rolas', 'rolei', 'rolem', 'roles', 'rolha', 
                              'rolos', 'rolou', 'rombo', 'rompa', 'rompe', 'rompi', 'rompo', 
                              'rompe', 'romas', 'ronca', 'ronco', 'ronca', 'ronda', 'ronde', 
                              'rondo', 'ronda', 'roque', 'rosas', 'rosca', 'rosna', 'rosne', 
                              'rosno', 'rosna', 'rosto', 'rotas', 'rotea', 'rotos', 'rouba', 
                              'roube', 'roubo', 'rouba', 'rouca', 'rouco', 'roupa', 'roxas', 
                              'roxos', 'rocai', 'rocam', 'rocar', 'rocas', 'rocou', 'roiam', 
                              'roias', 'roida', 'roido', 'rubis', 'rublo', 'rubra', 'rubro', 
                              'rudes', 'ruela', 'rufai', 'rufam', 'rufar', 'rufas', 'rufei', 
                              'rufem', 'rufes', 'rufou', 'rugai', 'rugam', 'rugar', 'rugas', 
                              'rugia', 'rugir', 'rugis', 'rugiu', 'rugou', 'rugue', 'ruiam', 
                              'ruias', 'ruido', 'ruimo', 'ruins', 'ruira', 'ruira', 'ruiva', 
                              'ruivo', 'rujam', 'rujas', 'rumai', 'rumam', 'rumar', 'rumas', 
                              'rumei', 'rumem', 'rumes', 'rumor', 'rumos', 'rumou', 'rural', 
                              'rusga', 'russa', 'russo', 'ruido', 'ruina', 'radio', 'redea', 
                              'regia', 'regio', 'regua', 'rieis', 'rocio', 'rosea', 'roseo', 
                              'saara', 'sabei', 'sabem', 'saber', 'sabes', 'sabia', 'sabor', 
                              'sabre', 'sabao', 'sacai', 'sacam', 'sacar', 'sacas', 'sacia', 
                              'sacie', 'sacio', 'sacis', 'sacia', 'sacos', 'sacou', 'sacra', 
                              'sacro', 'sadia', 'sadio', 'safai', 'safam', 'safar', 'safas', 
                              'safei', 'safem', 'safes', 'safou', 'safra', 'sagas', 'sagaz', 
                              'sagra', 'sagre', 'sagro', 'sagra', 'saiam', 'saias', 'saiba', 
                              'saido', 'saira', 'salas', 'salda', 'salde', 'saldo', 'salda', 
                              'sales', 'salga', 'salgo', 'salga', 'salmo', 'salsa', 'salta', 
                              'salte', 'salto', 'salta', 'salva', 'salve', 'salvo', 'salva', 
                              'salao', 'samba', 'sambe', 'sambo', 'samba', 'sanai', 'sanam', 
                              'sanar', 'sanas', 'sanei', 'sanem', 'sanes', 'sanea', 'sanha', 
                              'sanou', 'santa', 'santo', 'sapos', 'saque', 'sarai', 'saram', 
                              'sarar', 'saras', 'sarda', 'sarei', 'sarem', 'sares', 'sarna', 
                              'sarou', 'sarca', 'sauda', 'sauna', 'saxao', 'saiam', 'saias', 
                              'saida', 'saido', 'saimo', 'saira', 'sauda', 'saude', 'saudo', 
                              'sauva', 'seara', 'sebes', 'sebos', 'secai', 'secam', 'secar', 
                              'secas', 'secos', 'secou', 'sedas', 'sedes', 'sedia', 'sedie', 
                              'sedio', 'sedia', 'seduz', 'segue', 'segui', 'seios', 'seita', 
                              'seiva', 'seixo', 'sejam', 'sejas', 'selai', 'selam', 'selar', 
                              'selas', 'selei', 'selem', 'seles', 'selim', 'selos', 'selou', 
                              'selva', 'semea', 'senda', 'sendo', 'senha', 'senos', 'senso', 
                              'senta', 'sente', 'senti', 'sento', 'senta', 'senao', 'seque', 
                              'serei', 'serem', 'seres', 'seria', 'serie', 'serio', 'seria', 
                              'serra', 'serre', 'serro', 'serra', 'serva', 'serve', 'servi', 
                              'servo', 'serze', 'serzi', 'seras', 'serao', 'sesta', 'setas', 
                              'setor', 'sexos', 'sexta', 'sexto', 'secao', 'sifao', 'sigam', 
                              'sigas', 'sigla', 'sigma', 'signo', 'silos', 'silva', 'silve', 
                              'silvo', 'silva', 'simao', 'sinal', 'sinas', 'sinos', 'sinta', 
                              'sinto', 'siris', 'sirva', 'sirvo', 'sirza', 'sirzo', 'sisma', 
                              'sisme', 'sismo', 'sisma', 'sitas', 'sitia', 'sitie', 'sitio', 
                              'sitia', 'sitos', 'situa', 'situe', 'situo', 'situa', 'soado', 
                              'soais', 'soamo', 'soara', 'soara', 'soava', 'sobem', 'sobes', 
                              'sobra', 'sobre', 'sobro', 'sobra', 'socai', 'socam', 'socar', 
                              'socas', 'socos', 'socou', 'soeis', 'soemo', 'sofra', 'sofre', 
                              'sofri', 'sofro', 'sofre', 'sofas', 'sogra', 'sogro', 'solai', 
                              'solam', 'solar', 'solas', 'solda', 'solde', 'soldo', 'solda', 
                              'solei', 'solem', 'soles', 'solos', 'solou', 'solta', 'solte', 
                              'solto', 'solta', 'somai', 'somam', 'somar', 'somas', 'somei', 
                              'somem', 'somes', 'somos', 'somou', 'sonda', 'sonde', 'sondo', 
                              'sonda', 'sonha', 'sonhe', 'sonho', 'sonha', 'sonos', 'sonsa', 
                              'sonso', 'sopas', 'sopra', 'sopre', 'sopro', 'sopra', 'sopes', 
                              'soque', 'soros', 'sorri', 'sorta', 'sorte', 'sorti', 'sorva', 
                              'sorve', 'sorvi', 'sorvo', 'sorve', 'soube', 'sousa', 'souza', 
                              'sovai', 'sovam', 'sovar', 'sovas', 'sovei', 'sovem', 'soves', 
                              'sovou', 'suada', 'suado', 'suais', 'suamo', 'suara', 'suara', 
                              'suava', 'suave', 'subam', 'subas', 'subia', 'subir', 'subis', 
                              'subiu', 'sucos', 'sudao', 'sueca', 'sueco', 'sueis', 'suemo', 
                              'sugai', 'sugam', 'sugar', 'sugas', 'sugou', 'sugue', 'sujai', 
                              'sujam', 'sujar', 'sujas', 'sujei', 'sujem', 'sujes', 'sujos', 
                              'sujou', 'sulca', 'sulco', 'sulca', 'sulfa', 'sumam', 'sumas', 
                              'sumia', 'sumir', 'sumis', 'sumiu', 'sunga', 'super', 'supor', 
                              'supra', 'supre', 'supri', 'supro', 'supus', 'supos', 'supoe', 
                              'surda', 'surdo', 'surge', 'surgi', 'surja', 'surjo', 'surra', 
                              'surre', 'surro', 'surra', 'surta', 'surte', 'surto', 'susta', 
                              'suste', 'susti', 'susto', 'susta', 'suste', 'sutil', 'sutis', 
                              'sutia', 'suina', 'suino', 'suica', 'suico', 'sabia', 'sabio', 
                              'sepia', 'seria', 'serie', 'serio', 'semen', 'silex', 'simio', 
                              'siria', 'sirio', 'sitio', 'socia', 'socio', 'sodio', 'sosia', 
                              'sotao', 
                              'tabas', 'tacai', 'tacam', 'tacar', 'tacas', 'tacha', 'tache', 
                              'tacho', 'tacha', 'tacos', 'tacou', 'taipa', 'talas', 'talco', 
                              'talha', 'talhe', 'talho', 'talha', 'talos', 'talao', 'tampa', 
                              'tampe', 'tampo', 'tampa', 'tanga', 'tange', 'tangi', 'tango', 
                              'tange', 'tanja', 'tanjo', 'tanta', 'tanto', 'tanta', 'tapai', 
                              'tapam', 'tapar', 'tapas', 'tapei', 'tapem', 'tapes', 'tapea', 
                              'tapou', 'tapao', 'taque', 'taras', 'tarda', 'tarde', 'tardo', 
                              'tarda', 'tarja', 'tatea', 'tatua', 'tatue', 'tatuo', 'tatus', 
                              'tatua', 'taxai', 'taxam', 'taxar', 'taxas', 'taxei', 'taxem', 
                              'taxes', 'taxou', 'tacas', 'tecei', 'tecem', 'tecer', 'teces', 
                              'teceu', 'tecia', 'tecla', 'tecle', 'teclo', 'tecla', 'teias', 
                              'teima', 'teime', 'teimo', 'teima', 'telas', 'teles', 'telha', 
                              'telao', 'temam', 'temas', 'temei', 'temem', 'temer', 'temes', 
                              'temeu', 'temia', 'temor', 'temos', 'tempo', 'tenaz', 'tenda', 
                              'tende', 'tendi', 'tendo', 'tende', 'tenha', 'tenho', 'tenor', 
                              'tenra', 'tenro', 'tensa', 'tenso', 'tenta', 'tente', 'tento', 
                              'tenta', 'terei', 'terem', 'teres', 'teria', 'termo', 'terna', 
                              'terno', 'terra', 'teras', 'terao', 'terca', 'terco', 'tesas', 
                              'teses', 'tesos', 'testa', 'teste', 'testo', 'testa', 'tesao', 
                              'tetas', 'tetos', 'texto', 'tecam', 'tecas', 'tiara', 'tidas', 
                              'tidos', 'tiete', 'tigre', 'times', 'timao', 'tinam', 'tinas', 
                              'tinem', 'tines', 'tingi', 'tinha', 'tinia', 'tinir', 'tinis', 
                              'tiniu', 'tinja', 'tinjo', 'tinta', 'tinto', 'tipos', 'tirai', 
                              'tiram', 'tirar', 'tiras', 'tirei', 'tirem', 'tires', 'tiros', 
                              'tirou', 'titia', 'titio', 'titas', 'tiver', 'ticao', 'toada', 
                              'tocai', 'tocam', 'tocar', 'tocas', 'tocha', 'tocou', 'todas', 
                              'todos', 'togas', 'tolas', 'toldo', 'tolha', 'tolhe', 'tolhi', 
                              'tolho', 'tolhe', 'tolos', 'tomai', 'tomam', 'tomar', 'tomas', 
                              'tomba', 'tombe', 'tombo', 'tomba', 'tomei', 'tomem', 'tomes', 
                              'tomou', 'tomas', 'tonel', 'tonta', 'tonto', 'topai', 'topam', 
                              'topar', 'topas', 'topei', 'topem', 'topes', 'topos', 'topou', 
                              'toque', 'toras', 'torce', 'torci', 'torce', 'torna', 'torne', 
                              'torno', 'torna', 'toros', 'torpe', 'torra', 'torre', 'torro', 
                              'torra', 'torta', 'torto', 'torca', 'torco', 'tosai', 'tosam', 
                              'tosar', 'tosas', 'tosca', 'tosco', 'tosei', 'tosem', 'toses', 
                              'tosou', 'tosse', 'tossi', 'tosta', 'toste', 'tosto', 'tosta', 
                              'total', 'totem', 'touca', 'touro', 'trace', 'traem', 'traga', 
                              'trago', 'traga', 'traia', 'traio', 'trair', 'trais', 'traiu', 
                              'traja', 'traje', 'trajo', 'traja', 'trama', 'trapo', 'trara', 
                              'trata', 'trate', 'trato', 'trata', 'trava', 'trave', 'travo', 
                              'trava', 'traze', 'traze', 'traca', 'traco', 'traca', 'traia', 
                              'trais', 'treco', 'trema', 'treme', 'tremi', 'tremo', 'treme', 
                              'trena', 'trens', 'treno', 'trepa', 'trepe', 'trepo', 'trepa', 
                              'treta', 'treva', 'trevo', 'treze', 'tribo', 'trico', 'trigo', 
                              'trina', 'trino', 'trios', 'tripa', 'troca', 'troce', 'troco', 
                              'troca', 'trono', 'tropa', 'trota', 'trote', 'troto', 'trota', 
                              'trova', 'troca', 'troco', 'troca', 'truco', 'trufa', 'truta', 
                              'troia', 'tubos', 'tufao', 'tumba', 'tumor', 'tupis', 'turba', 
                              'turbe', 'turbo', 'turba', 'turca', 'turco', 'turma', 'turno', 
                              'turne', 'turva', 'turve', 'turvo', 'turva', 'tussa', 'tusso', 
                              'tutor', 'tabua', 'taxis', 'tedio', 'tenis', 'tenue', 'tibia', 
                              'tibio', 'tinge', 'torax', 'torio', 'tunel', 
                              'ufana', 'ufane', 'ufano', 'ufana', 'uivai', 'uivam', 'uivar', 
                              'uivas', 'uivei', 'uivem', 'uives', 'uivos', 'uivou', 'ultra',
                              'ulula', 'ulule', 'ululo', 'ulula', 'unais', 'unemo', 'ungem', 
                              'unges', 'ungia', 'ungir', 'ungis', 'ungiu', 'unhas', 'uniam', 
                              'unias', 'unida', 'unido', 'unimo', 'unira', 'unira', 'uniao', 
                              'untai', 'untam', 'untar', 'untas', 'untei', 'untem', 'untes', 
                              'untou', 'uncao', 'urano', 'urdam', 'urdas', 'urdem', 'urdes', 
                              'urdia', 'urdir', 'urdis', 'urdiu', 'urgia', 'urgir', 'urgis', 
                              'urgiu', 'urina', 'urine', 'urino', 'urina', 'urjam', 'urjas', 
                              'urnas', 'urrai', 'urram', 'urrar', 'urras', 'urrei', 'urrem', 
                              'urres', 'urros', 'urrou', 'ursas', 'ursos', 'urubu', 'ureia', 
                              'usada', 'usado', 'usais', 'usamo', 'usara', 'usara', 'usava', 
                              'useis', 'usemo', 'usina', 'usual', 'usura', 
                              'vacas', 'vades', 'vadea', 'vadia', 'vadie', 'vadio', 'vadia', 
                              'vagai', 'vagam', 'vagar', 'vagas', 'vagem', 'vagia', 'vagir', 
                              'vagis', 'vagiu', 'vagos', 'vagou', 'vague', 'vagao', 'vaiai', 
                              'vaiam', 'vaiar', 'vaias', 'vaiei', 'vaiem', 'vaies', 'vaiou', 
                              'valas', 'valei', 'valem', 'valer', 'vales', 'valeu', 'valha', 
                              'valho', 'valia', 'valor', 'valos', 'valsa', 'vamos', 'vapor', 
                              'varai', 'varam', 'varar', 'varas', 'varei', 'varem', 'vares', 
                              'varia', 'varie', 'vario', 'varia', 'varou', 'varra', 'varre', 
                              'varri', 'varro', 'varre', 'varao', 'vasos', 'vasta', 'vasto', 
                              'vazai', 'vazam', 'vazar', 'vazas', 'vazei', 'vazem', 'vazes', 
                              'vazia', 'vazio', 'vazou', 'vazao', 'veado', 'vedai', 'vedam', 
                              'vedar', 'vedas', 'vedei', 'vedem', 'vedes', 'vedou', 'veias', 
                              'vejai', 'vejam', 'vejas', 'velai', 'velam', 'velar', 'velas', 
                              'velei', 'velem', 'veles', 'velha', 'velho', 'velou', 'veloz', 
                              'vemos', 'venal', 'vence', 'venci', 'vence', 'venda', 'vende', 
                              'vendi', 'vendo', 'venda', 'vende', 'venha', 'venho', 'venta', 
                              'vente', 'vento', 'venta', 'venca', 'venco', 'verba', 'verbo', 
                              'verde', 'verei', 'verem', 'veres', 'verga', 'veria', 'verme', 
                              'versa', 'verse', 'verso', 'versa', 'verta', 'verte', 'verti', 
                              'verto', 'verte', 'veras', 'verao', 'vesga', 'vesgo', 'vespa', 
                              'veste', 'vesti', 'vetai', 'vetam', 'vetar', 'vetas', 'vetei', 
                              'vetem', 'vetes', 'vetor', 'vetou', 'vexai', 'vexam', 'vexar', 
                              'vexas', 'vexei', 'vexem', 'vexes', 'vexou', 'vezes', 'viaja', 
                              'viaje', 'viajo', 'viaja', 'viana', 'vibra', 'vibre', 'vibro', 
                              'vibra', 'vicia', 'vicie', 'vicio', 'vicia', 'vidas', 'vidra', 
                              'vidre', 'vidro', 'vidra', 'viela', 'viena', 'viera', 'vieza', 
                              'vigas', 'vigia', 'vigie', 'vigio', 'vigia', 'vigor', 'vilas', 
                              'vilao', 'vilas', 'vimos', 'vinca', 'vinco', 'vinca', 'vinda', 
                              'vinde', 'vindo', 'vinga', 'vingo', 'vinga', 'vinha', 'vinho', 
                              'vinte', 'viola', 'viole', 'violo', 'viola', 'virai', 'viram', 
                              'virar', 'viras', 'virei', 'virem', 'vires', 'viria', 'viril', 
                              'viris', 'virmo', 'virou', 'viras', 'virao', 'visai', 'visam', 
                              'visar', 'visas', 'visei', 'visem', 'vises', 'visou', 'visse', 
                              'vista', 'viste', 'visto', 'visao', 'vital', 'viuva', 'viuve', 
                              'viuvo', 'viuva', 'vivam', 'vivas', 'vivaz', 'vivei', 'vivem', 
                              'viver', 'vives', 'viveu', 'vivia', 'vivos', 'vioes', 'viuva', 
                              'viuvo', 'voado', 'voais', 'voamo', 'voara', 'voara', 'voava', 
                              'voces', 'vodca', 'voeis', 'voemo', 'vogal', 'volta', 'volte', 
                              'volto', 'volta', 'volva', 'volve', 'volvi', 'volvo', 'volve', 
                              'voraz', 'vossa', 'vosso', 'votai', 'votam', 'votar', 'votas', 
                              'votei', 'votem', 'votes', 'votos', 'votou', 'vovos', 'vovos', 
                              'vozes', 'vulgo', 'vulto', 'vulva', 'vacuo', 'varia', 'venia', 
                              'vicio', 'video', 'vieis', 'virus', 'volei', 
                              'xales', 'xaras', 'xelim', 'xeque', 'xerox', 'xiita', 'xinga', 
                              'xingo', 'xinga', 'xisto', 'xucra', 'xucro', 'xerox', 
                              'zagas', 'zanga', 'zango', 'zanga', 'zanza', 'zanze', 'zanzo', 
                              'zanza', 'zarpa', 'zarpe', 'zarpo', 'zarpa', 'zebra', 'zelai', 
                              'zelam', 'zelar', 'zelas', 'zelei', 'zelem', 'zeles', 'zelou', 
                              'zerai', 'zeram', 'zerar', 'zeras', 'zerei', 'zerem', 'zeres', 
                              'zeros', 'zerou', 'zinco', 'zomba', 'zombe', 'zombo', 'zomba', 
                              'zonas', 'zonza', 'zonzo', 'zumba', 'zumbe', 'zumbi', 'zumbo', 
                              'zunam', 'zunas', 'zunem', 'zunes', 'zunia', 'zunir', 'zunis', 
                              'zuniu', 'zurra', 'zurre', 'zurro', 'zurra', 'ziper', 
                              'abaco', 'acaro', 'acida', 'acido', 'agape', 'agata', 'ageis', 
                              'agios', 'aguas', 'aguia', 'alamo', 'album', 'alibi', 'apice', 
                              'arabe', 'ardua', 'arduo', 'areas', 'arias', 'arida', 'arido', 
                              'atomo', 'atona', 'atono', 'atrio', 'aurea', 'aureo', 'avida', 
                              'avido', 'azimo', 'amago', 'ambar', 'animo', 'anodo', 'ansia', 
                              'ebano', 'ebrio', 'eguas', 'epica', 'epico', 'epoca', 'ereis', 
                              'esima', 'esimo', 'etica', 'etico', 'emula', 'emulo', 'exito', 
                              'exodo', 'iamos', 'icone', 'idolo', 'ignea', 'igneo', 'impar', 
                              'impia', 'impio', 'india', 'indio', 'italo', 'itens', 'obito', 
                              'obolo', 'obvia', 'obvio', 'odios', 'oleos', 'opera', 'orfao', 
                              'orfas', 'orgao', 'ossea', 'osseo', 'otica', 'otico', 'otima', 
                              'otimo', 'ovulo', 'oxido', 'umida', 'umido', 'unica', 'unico', 
                              'urico', 'uteis', 'utero']
        
        self.a+=1
        self.Palavra_Secreta = random.choices(self.Palavras_5letras, k=1)
        self.Palavra_Secreta = self.Palavra_Secreta[0]
        self.Palavra_Secreta = self.Palavra_Secreta.upper()
        self.Palavra_Tentada = "*****"
        self.Cont = 0
        
        self.letra11.text = "-"
        self.letra11.color = "gray"
        self.letra12.text = "-"
        self.letra12.color = "gray"
        self.letra13.text = "-"
        self.letra13.color = "gray"
        self.letra14.text = "-"
        self.letra14.color = "gray"
        self.letra15.text = "-"
        self.letra15.color = "gray"
        
        self.letra21.text = "-"
        self.letra21.color = "gray"
        self.letra22.text = "-"
        self.letra22.color = "gray"
        self.letra23.text = "-"
        self.letra23.color = "gray"
        self.letra24.text = "-"
        self.letra24.color = "gray"
        self.letra25.text = "-"
        self.letra25.color = "gray"
        
        self.letra31.text = "-"
        self.letra31.color = "gray"
        self.letra32.text = "-"
        self.letra32.color = "gray"
        self.letra33.text = "-"
        self.letra33.color = "gray"
        self.letra34.text = "-"
        self.letra34.color = "gray"
        self.letra35.text = "-"
        self.letra35.color = "gray"
        
        self.letra41.text = "-"
        self.letra41.color = "gray"
        self.letra42.text = "-"
        self.letra42.color = "gray"
        self.letra43.text = "-"
        self.letra43.color = "gray"
        self.letra44.text = "-"
        self.letra44.color = "gray"
        self.letra45.text = "-"
        self.letra45.color = "gray"
        
        self.letra51.text = "-"
        self.letra51.color = "gray"
        self.letra52.text = "-"
        self.letra52.color = "gray"
        self.letra53.text = "-"
        self.letra53.color = "gray"
        self.letra54.text = "-"
        self.letra54.color = "gray"
        self.letra55.text = "-"
        self.letra55.color = "gray"
        
        self.letra61.text = "-"
        self.letra61.color = "gray"
        self.letra62.text = "-"
        self.letra62.color = "gray"
        self.letra63.text = "-"
        self.letra63.color = "gray"
        self.letra64.text = "-"
        self.letra64.color = "gray"
        self.letra65.text = "-"
        self.letra65.color = "gray"
        
        self.resultado.text = ""
        self.nletras.text = "A palavra não contem: "
        self.palavra.text = "Digite sua palavra aqui"
        
        self.botaosortear.text = "QUAL PALAVRA"
        
    def Checar(self, instance):
        if self.a == 0:
            self.resultado.text = "Você não sorteou a palavra (botão azul)"
        else:    
            self.Ncontem = []
            self.Palavra_Tentada = self.palavra.text[:5]
            self.Palavra_Tentada = self.Palavra_Tentada.upper()
            if len(self.Palavra_Tentada) < 5:
                self.resultado.text = "A palavra digitada não tem 5 letras, digite outra!"
            else:
                self.Cont+=1
                if self.Cont < 7:
                    
                    Descoberta = ["-", "-", "-", "-", "-"]
                   
                    Lista_PT = []
                    for letra in self.Palavra_Tentada[:5]:
                        Lista_PT.append(letra)
        
                    Lista_PS = []
                    for letra in self.Palavra_Secreta:
                        Lista_PS.append(letra)
                        
                    Compara = {}
                    i = 0
                    while i < 5:
                        Compara[i] = []
                        j = 0
                        while j < 5:
                            if Lista_PT[i] == Lista_PS[j]:
                                Compara[i].append(True)
                            else:
                                Compara[i].append(False)
                            j+=1
                        i+=1
                   
                    i=0
                    while i < 5:
                        if Compara[i][i] == True:
                            Descoberta[i] = self.Palavra_Tentada[i]
                            j=0
                            while j < 5:
                                if j != i:
                                    Compara[i][j] = False
                                j+=1
                            k=0
                            while k < 5:
                                if k != i:
                                    Compara [k][i] = False
                                k+=1
                        i+=1
                     
                    i=0
                    while i < 5:
                        j=0
                        while j < 5:
                            if Compara[i][j] == True and i != j:
                                Descoberta[i] = self.Palavra_Tentada[i].lower()
                                k=i+1
                                while k<5:
                                    if k != j:
                                        Compara[k][j] = False
                                    k+=1
                                l=j+1
                                while l<5:
                                    if l != i:
                                        Compara[i][l] = False
                                    l+=1
                            j+=1
                        i+=1
                   
                    AA = set(Lista_PS)
                       
                    BB = set(Lista_PT)
                   
                    C = BB.difference(AA)
                    for letra in C:
                        self.Ncontem.append(letra)
                    
                    self.Ncontem = sorted(set(self.Ncontem))
                    for i in range(len(self.Ncontem)):
                        self.nletras.text = self.nletras.text+"-"+self.Ncontem[i]
                    
                    self.letra61.text = self.letra51.text
                    self.letra62.text = self.letra52.text
                    self.letra63.text = self.letra53.text
                    self.letra64.text = self.letra54.text
                    self.letra65.text = self.letra55.text
                    
                    self.letra51.text = self.letra41.text
                    self.letra52.text = self.letra42.text
                    self.letra53.text = self.letra43.text
                    self.letra54.text = self.letra44.text
                    self.letra55.text = self.letra45.text
                    
                    self.letra41.text = self.letra31.text
                    self.letra42.text = self.letra32.text
                    self.letra43.text = self.letra33.text
                    self.letra44.text = self.letra34.text
                    self.letra45.text = self.letra35.text
                    
                    self.letra31.text = self.letra21.text
                    self.letra32.text = self.letra22.text
                    self.letra33.text = self.letra23.text
                    self.letra34.text = self.letra24.text
                    self.letra35.text = self.letra25.text
                    
                    self.letra21.text = self.letra11.text
                    self.letra22.text = self.letra12.text
                    self.letra23.text = self.letra13.text
                    self.letra24.text = self.letra14.text
                    self.letra25.text = self.letra15.text
                    
                    self.letra61.color = self.letra51.color
                    self.letra62.color = self.letra52.color
                    self.letra63.color = self.letra53.color
                    self.letra64.color = self.letra54.color
                    self.letra65.color = self.letra55.color
                    
                    self.letra51.color = self.letra41.color
                    self.letra52.color = self.letra42.color
                    self.letra53.color = self.letra43.color
                    self.letra54.color = self.letra44.color
                    self.letra55.color = self.letra45.color
                    
                    self.letra41.color = self.letra31.color
                    self.letra42.color = self.letra32.color
                    self.letra43.color = self.letra33.color
                    self.letra44.color = self.letra34.color
                    self.letra45.color = self.letra35.color
                    
                    self.letra31.color = self.letra21.color
                    self.letra32.color = self.letra22.color
                    self.letra33.color = self.letra23.color
                    self.letra34.color = self.letra24.color
                    self.letra35.color = self.letra25.color
                    
                    self.letra21.color = self.letra11.color
                    self.letra22.color = self.letra12.color
                    self.letra23.color = self.letra13.color
                    self.letra24.color = self.letra14.color
                    self.letra25.color = self.letra15.color
                    
                    self.letra11.text = Descoberta[0].upper()
                    if Descoberta[0] == "-":
                        self.letra11.color = "red"
                    elif Descoberta[0].islower():
                        self.letra11.color = "gold"
                    else:
                        self.letra11.color = "chartreuse"
                        
                    self.letra12.text = Descoberta[1].upper()
                    if Descoberta[1] == "-":
                        self.letra12.color = "red"
                    elif Descoberta[1].islower():
                        self.letra12.color = "gold"
                    else:
                        self.letra12.color = "chartreuse"
                        
                    self.letra13.text = Descoberta[2].upper()
                    if Descoberta[2] == "-":
                        self.letra13.color = "red"
                    elif Descoberta[2].islower():
                        self.letra13.color = "gold"
                    else:
                        self.letra13.color = "chartreuse"
                        
                    self.letra14.text = Descoberta[3].upper()
                    if Descoberta[3] == "-":
                        self.letra14.color = "red"
                    elif Descoberta[3].islower():
                        self.letra14.color = "gold"
                    else:
                        self.letra14.color = "chartreuse"
                        
                    self.letra15.text = Descoberta[4].upper()
                    if Descoberta[4] == "-":
                        self.letra15.color = "red"
                    elif Descoberta[4].islower():
                        self.letra15.color = "gold"
                    else:
                        self.letra15.color = "chartreuse"
                      
                    self.palavra.text = ""
                    self.resultado.text = "Você ainda não acertou. Digite outra palavra!"
                    
                if self.Palavra_Tentada == self.Palavra_Secreta:
                    if self.Cont == 1:
                        self.resultado.text = "PICA DAS PALAVRAS!!!! Acertou na Primeira."
                        self.palavra.text = "Aperte o botão azul para jogar de novo"
                        self.botaosortear.text = "QUAL PALAVRA - aperte aqui e jogue novamente"
                            
                    elif self.Cont == 2:
                        self.resultado.text = "GENIAL!!!! Acertou em 2 tentativas."
                        self.palavra.text = "Aperte o botão azul para jogar de novo"
                        self.botaosortear.text = "QUAL PALAVRA - aperte aqui e jogue novamente"
                            
                    elif self.Cont == 3:
                        self.resultado.text = "ESPETACULAR!!!! Acertou em 3 tentativas."
                        self.palavra.text = "Aperte o botão azul para jogar de novo"
                        self.botaosortear.text = "QUAL PALAVRA - aperte aqui e jogue novamente"
                        
                    elif self.Cont == 4:
                        self.resultado.text = "MUITO BEM!!!! Acertou em 4 tentativas"
                        self.palavra.text = "Aperte o botão azul para jogar de novo"
                        self.botaosortear.text = "QUAL PALAVRA - aperte aqui e jogue novamente"
                        
                    elif self.Cont == 5:
                        self.resultado.text = "Mandou BEM!!!! Acertou em 5 tentativas"
                        self.palavra.text = "Aperte o botão azul para jogar de novo"
                        self.botaosortear.text = "QUAL PALAVRA - aperte aqui e jogue novamente"
                        
                    elif self.Cont == 6:
                        self.resultado.text = "Você foi REGULAR!!! Acertou em 6 tentativas"
                        self.palavra.text = "Aperte o botão azul para jogar de novo"
                        self.botaosortear.text = "QUAL PALAVRA - aperte aqui e jogue novamente"
                         
                if self.Palavra_Tentada != self.Palavra_Secreta and self.Cont == 6:
                    self.resultado.text = "Você perdeu. A palavra secreta era: "+self.Palavra_Secreta
                    self.palavra.text = "Aperte o botão azul para jogar de novo"
                    self.botaosortear.text = "QUAL PALAVRA - aperte aqui e jogue novamente"
                    
                    
    def build(self):
        self.window = GridLayout(
            cols = 1,
            row_force_default=True,
            row_default_height=100,
            #col_force_default=True,
            #col_defaul_width=500
            )
        self.window.siz_hint = (1, 1)
        self.window.po_hint = {"center_x": 0.5, "center_y": 0.5}
        self.window.spacing = [10,10]
        
        self.botaosortear = Button(
            text = "QUAL PALAVRA - Aperte aqui para jogar",
            font_size = 30,
            bold = True,
            background_color = "blue",
            background_normal = "",
            halign = 'center',
            valign = 'center'
            )
        self.botaosortear.bind(on_press=self.Sortear)
        self.window.add_widget(self.botaosortear)
        
        """
        self.titulo = Label(
            text = "QUAL PALAVRA?",
            font_size = 32,
            color = "blue",
            bold = True,
            halign = 'center',
            valign = 'center',
            )
        self.window.add_widget(self.titulo)
        
        
        self.window.add_widget(Image(source="QualPalavra.png",
                                     height = 150,
                                     size_hint_y = None,
                                     size_hint_x = 0.5,
                                     allow_stretch = True
                                     ))
        """
        
        self.palavra = TextInput(
            text = "Aperte o botão azul para jogar",
            multiline = False,
            padding_y = (25,25),
            #padding_x = (10,10),
            size_hint = (1,1),
            font_size = 30,
            halign = 'center'
            )
        self.window.add_widget(self.palavra)
          
        self.resultado = Label(
            text = "-",
            font_size = 32,
            color = "green",
            bold = True,
            halign = 'center',
            valign = 'center',
            )
        self.window.add_widget(self.resultado)
        
        self.botaochecar = Button(
            text = "CHECAR PALAVRA DIGITADA",
            font_size = 30,
            bold = True,
            background_color = "green",
            background_normal = "",
            halign = 'center',
            valign = 'center'
            )
        self.botaochecar.bind(on_press=self.Checar)
        self.window.add_widget(self.botaochecar)
        
        
        self.nletras = Label(
            text = "A palavra não contem: ",
            font_size = 25,
            color = "red",
            bold = True,
            halign = 'center',
            valign = 'center',
            )
        self.window.add_widget(self.nletras)
        
        self.childrenwindow = GridLayout(
            cols = 5,
            #row_force_default=True,
            #row_default_height=50,
            #col_force_default=True,
            #col_default_width=50
            )
        self.childrenwindow.siz_hint = (1, 1)
        self.childrenwindow.spacing = [25,25]
            
        self.letra11 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra11)
        
        self.letra12 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra12)
        
        self.letra13 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra13)
        
        self.letra14 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra14)
        
        self.letra15 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center'
            )
        self.childrenwindow.add_widget(self.letra15)
        
        self.letra21 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra21)
        
        self.letra22 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra22)
        
        self.letra23 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra23)
        
        self.letra24 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra24)
        
        self.letra25 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center'
            )
        self.childrenwindow.add_widget(self.letra25)
        
        self.letra31 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra31)
        
        self.letra32 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra32)
        
        self.letra33 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra33)
        
        self.letra34 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra34)
        
        self.letra35 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center'
            )
        self.childrenwindow.add_widget(self.letra35)
        
        self.letra41 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra41)
        
        self.letra42 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra42)
        
        self.letra43 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra43)
        
        self.letra44 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra44)
        
        self.letra45 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center'
            )
        self.childrenwindow.add_widget(self.letra45)
        
        self.letra51 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra51)
        
        self.letra52 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra52)
        
        self.letra53 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra53)
        
        self.letra54 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra54)
        
        self.letra55 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center'
            )
        self.childrenwindow.add_widget(self.letra55)
        
        self.letra61 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra61)
        
        self.letra62 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra62)
        
        self.letra63 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra63)
        
        self.letra64 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center',
            )
        self.childrenwindow.add_widget(self.letra64)
        
        self.letra65 = Label(
            text = "-",
            font_size = 30,
            color = "grey",
            halign = 'center',
            valign = 'center'
            )
        self.childrenwindow.add_widget(self.letra65)
        
        self.window.add_widget(self.childrenwindow)   
        
        return self.window
    
if __name__ == "__main__":
    Qual_Palavra().run()