# coding:utf-8

import flask 
# import datetime

REFERENCE={
'greek29'       :"Wikipedia. 生命の起源. (最終アクセス 2013/09/03)",#a01
'greek14'       :"Wikipedia. ヘレニズム. (最終アクセス  2013/08/26)",#a02
'med2'          :"Wikipedia. グノーシス主義. (最終アクセス 2013/09/03)",#a03
'ana2'          :"Wikipedia. Ordinary language  school.  (最終アクセス 2013/09/03)",#a04
'ana4'          :"Wikipedia. Wittgenstein on  Russell's   Paradox.     (最終アクセス 2013/09/03)",#a05
'greek2'        :"Stanford Encyclopedia of Philosophy. Zeno of Elea.    (最終アクセス 2013/09/03)",#a05
'ana5'          :"Stanford Encyclopedia of Philosophy. Wittgenstein's Logical Atomism. (最終アクセス 2013/09/03)",#a06
'fr1'           :"Stanford Encyclopedia of Philosophy. Deleuze.  (最終アクセス 2013/09/03)",#a01
'ana1'          :"McDowell     J.  1984    'Wittgenstein   on  Following   a   Rule'       Synthese    58:325-364",#002
'greek1'        :"Plato    (著)・Grube       G.  M.  A.(翻訳).『Plato   Five    Dialogues   :   Euthyphro       Apology     Crito       Meno        Phaedo』、Hackett Pub Co  Inc.、2002",#003
'ana3'          :"Thompson     C.  1997    'Wittgenstein       Tolstoy and the meaning of  life'       Philosophical   Investigations、20(2)        97–116",#004
'greek20'       :"天野正幸 (著)、『ギリシャ哲学―哲学の原点』、放送大学教育振興会、1999",#007
'greek3'        :"アリストテレス (著)・出隆(翻訳)、『形而上学〈上〉』、岩波書店、1959",#008
'greek3_1'      :"アリストテレス (著)・高田三郎(翻訳)、『ニコマコス倫理学〈上〉』、岩波書店、1971",#009
'greek3_2'      :"アリストテレス (著)・高田三郎(翻訳)、『ニコマコス倫理学〈下〉』、岩波書店、1973",#010
'de4'           :"有福孝岳ほか  (編集)、『カント事典』、弘文堂、1997",#011
'med1'          :"アンスコム,       G.  E.  M.ほか    (著)・野本和幸ほか(翻訳)、『哲学の三人―アリストテレス・トマス・フレーゲ』、岩波書店、1992",#012
'greek4'        :"アームソン,       J.  O.  (著)・雨宮健(翻訳)、『アリストテレスの倫理学入門』、岩波書店、2004",#013
'ana29'         :"飯田隆 (編集)、『ウィトゲンシュタイン読本』、法政大学出版局、1995",#014
'ana30'         :"飯田隆 (著)、『言語哲学大全〈1〉論理と言語』、勁草書房、1987",#015
'ana31'         :"飯田隆 (著)、『言語哲学大全〈2〉意味と様相 (上)』、勁草書房、1989",#016
'ana32'         :"飯田隆 (著)、『言語哲学大全〈3〉意味と様相 (下)』、   勁草書房、1995",#017
'ana33'         :"飯田隆 (著)、『言語哲学大全〈4〉真理と意味』、勁草書房、2002",#018
'hist25'        :"飯田隆 (編集)、『哲学の歴史〈11〉論理・数学・言語』、中央公論新社、2007",#019
'sci2'          :"伊勢田哲治   (著)、『疑似科学と科学の哲学 』、名古屋大学出版会、2003",#020
'sci3'          :"伊勢田哲治ほか (編集)、『科学技術をよく考える    クリティカル・シンキング練習帳』、名古屋大学出版会、2013",#021
'fr10'          :"市倉宏祐    (著)、『現代フランス思想への誘い―アンチ・オイディプスのかなたへ』、岩波書店、1986",#022
'other3'        :"今道友信    (編集)、『講座    美学  1   美学の歴史』、東京大学出版会、1984",#023
'fr2'           :"今村仁司ほか  (著)、『フーコー   (CenturyBooks―人と思想)』、清水書院、1999",#024
'ana14'         :"入不二基義   (著)、『ウィトゲンシュタイン 「私」は消去できるか』、日本放送出版協会、2006",#025
'de3'           :"岩崎武雄    (著)、『カント『純粋理性批判』の研究 』、勁草書房、1965",#026
'hist17'        :"岩崎武雄    (著)、『西洋哲学史』、有斐閣、1975",#027
'hist16'        :"岩崎允胤ほか  (編集)、『西洋哲学史概説』、有斐閣、1986",#028
'greek25'       :"岩田靖夫    (著)、『アリストテレスの倫理思想』、岩波書店、1985",#029
'hist1'         :"ウィル・バッキンガム  (著)・小須田健(翻訳)、『哲学大図鑑』、三省堂、2012",#030
'modern5'       :"上野修 (著)、『スピノザの世界―神あるいは自然』、講談社、2005",#031
'hist20'        :"生松敬三ほか  (編集)、『概念と歴史がわかる西洋哲学小辞典』、筑摩書房、2011",#032
'hist2'         :"ウォーバートン,    N.  (著)・船木亨(翻訳)、『入門 哲学の名著』、ナカニシヤ出版、2005",#033
'fr7'           :"宇野邦一    (著)、『ドゥルーズ  流動の哲学』、講談社、2001",#034
'ana6'          :"エイヤー,        A.  J.  (著)・信原幸弘(翻訳)、『ウィトゲンシュタイン』、みすず書房、1988",#035
'ana7'          :"エヴニン,        S.  (著)・宮島昭二(翻訳)、『デイヴィドソン―行為と言語の哲学』、勁草書房、1996",#036
'hist10'        :"大浦康介ほか  (編集)、『哲学を読む―考える愉しみのために』、人文書院、2000",#037
'fr5'           :"大城信哉    (著)、『図解雑学   ポスト構造主義』、ナツメ社、2005",#038
'fr6'           :"大城信哉    (著)・小野功生    (監修)、『図解雑学  ポスト構造主義』、ナツメ社、2005",#039
'ana16'         :"大庭健 (著)、『はじめての分析哲学』、産業図書、1990",#040
'modern7'       :"大橋良介    (編集)、『ドイツ観念論を学ぶ人のために』、世界思想社、2005",#041
'hist15'        :"岡崎文明ほか  (著)、『西洋哲学史  理性の運命と可能性』、講談社、1997",#042
'fr9'           :"岡本裕一朗   (著)、『ポストモダンの思想的根拠―9・11と管理社会』、ナカニシヤ出版、2005",#043
'sci1'          :"オカーシャ,   S.  (著)・廣瀬覚(翻訳)、『科学哲学』、岩波書店、2008",#044
'fr8'           :"小野功生    (監修)、『図解雑学  構造主義』、ナツメ社、2004",#045
'modern6'       :"加賀野井秀一  (著)、『知の教科書  ソシュール』、講談社、2004",#046
'greek18'       :"加来彰俊    (著)、『ソクラテスはなぜ死んだのか』、岩波書店、2004",#047
'indo4'         :"梶山雄一ほか  、『空の論理「中観」―仏教の思想〈3〉』、角川書店、1997",#048
'greek19'       :"加藤信朗    (著)、『ギリシャ哲学史』、東京大学出版会、1996",#049
'indo9'         :"金岡秀友    (著)、『インド哲学史概説』、佼成出版社、1990",#050
'exist8'        :"茅野良男        (著)、『実存主義入門―新しい生き方を求めて』、講談社、1968",#051
'indo8'         :"金倉圓照        (著)、『インド哲学史』、平楽寺書店      1987",#052
'greek5'        :"カーク,     G.  S.ほか    (著)・内山勝利ほか(翻訳)、『ソクラテス以前の哲学者たち   第二版』、京都大学学術出版会版、2006",#053
'modern1'       :"カーリー,        E.ほか    (著)、『スピノザ『エチカ』を読む』、文化書房博文社、1993",#054
'ana34'         :"鬼界彰夫    (著)、『ウィトゲンシュタインはこう考えた-哲学的思考の全軌跡1912~1951』、講談社、2003",#055
'hist18'        :"木田元 (著)、『反哲学史』、講談社学術文庫、2000",#056
'fr3'           :"北沢方邦    (著)、『構造主義』、講談社、1968",#057
'de5'           :"熊野純彦    (著)、『カント    世界の限界を経験することは可能か』、NHK出版、2002",#058
'fr15'          :"熊野純彦    (著)、『レヴィナス入門』、筑摩書房、1999",#059
'greek28'       :"熊野純彦    (著)、『西洋哲学史  古代から中世へ』、岩波書店、2006",#060
'de9'           :"黒崎政男    (著)、『カント『純粋理性批判』入門』、講談社、2000",#061
'ana35'         :"黒崎宏 (著)、『ウィトゲンシュタインと「独我論」』、勁草書房、2002",#062
'ana36'         :".1クワイン,W.V.O.(著)・飯田隆(翻訳)、『論理的観点から』、勁草書房、1992",#062
'hist12'        :"小阪修平ほか  (著)、『わかりたいあなたのための現代思想・入門』、宝島社、2000",#063
'hist11'        :"小林一郎    (著)、『西洋哲学史入門』、金港堂出版部、1998",#064
'sci7'          :"小林道夫    (著)、『科学哲学』、産業図書、1996",#065
'greek6'        :"コーンフォード,     F.  M.  (著)・山田道夫(翻訳)、『ソクラテス以前以後』、岩波文庫、1995",#066
'fr12'          :"桜井哲夫    (著)、『知の教科書  フーコー』、講談社、2001",#067
'greek27'       :"桜井万里子   (著)、『ギリシャ史』、中央公論新社、2005",#068
'exist5'        :"佐々木一義   (著)、『実存哲学入門』、関書院出版、1957",#069
'exist00'       :"サルトル,        J-P.    (著)・白井浩司(翻訳)、『サルトル全集 第8巻 恭しき娼婦』、人文書院、1982",#070
'exist0'        :"サルトル,        J-P.    (著)・白井浩司(翻訳)、『嘔吐』、人文書院、1994",#070
'exist1'        :"サルトル,        J-P.    (著)・松浪信三郎(翻訳)、『存在と無〈1〉現象学的存在論の試み    』、筑摩書房、2007",#070
'exist2'        :"サルトル,        J-P.    (著)・松浪信三郎(翻訳)、『存在と無〈2〉現象学的存在論の試み    』、筑摩書房、2007",#071
'exist3'        :"サルトル,        J-P.    (著)・松浪信三郎(翻訳)、『存在と無〈3〉現象学的存在論の試み    』、筑摩書房、2008",#072
'ana8'          :"サール,     J・R.    (著)・坂本百大ほか(翻訳)  『言語行為―言語哲学への試論』、勁草書房、1986",#073
'fr16'          :"篠原資明    (著)、『ドゥルーズ  ノマドロジー』、講談社、2005",#074
'ana22'         :"柴田正良    (著)、『ロボットの心-7つの哲学物語』、講談社、2001",#075
'hist4'         :"シュヴェーグラー    (著)・谷川徹三ほか(翻訳)、『西洋哲学史〈上〉』、岩波文庫、1995",#076
'other4'        :"砂田利一ほか  (著)、『数学者の哲学・哲学者の数学―歴史を通じ現代を生きる思索』、東京図書、2011",#077
'modern2'       :"スリュサレーヴァ,        H.  A.  (著)・谷口勇(翻訳)、『現代言語学とソシュール理論』、而立書房、1979",#078
'greek7'        :"セドレー,        D.  (著)・内山勝利(翻訳)、『古代ギリシア・ローマの哲学』、京都大学学術出版会、2009",#080
'other6'        :"高橋昌一郎   (著)、『理性の限界――不可能性・不確定性・不完全性』、講談社、2008",#081
'ana25'         :"竹尾治一郎   (著)、『分析哲学入門』、世界思想社、1999",#082
'hist21'        :"竹田青嗣    (著)、『現代思想の冒険』、筑摩書房、1992",#083
'phen6'         :"竹田青嗣    (著)、『現象学入門』、NHK出版、1989",#084
'indo7'         :"立川武蔵    (著)、『はじめてのインド哲学』、講談社、1992",#085
'greek30'       :"田中美知太郎、『ソフィスト』、講談社学術文庫、1976",#086
'phen7'         :"谷徹  (著)、『これが現象学だ』、講談社、2002",#087
'ana9'          :"ダメット,        M.  (著)・野本和幸(翻訳)、『分析哲学の起源―言語への転回』、勁草書房、1998",#088
'hist19'        :"杖下隆英ほか  (編集)、『テキストブック   西洋哲学史』、有斐閣、1984",#089
'ana10'         :"デイヴィドソン,     D.  (著)・津留竜馬(翻訳)、『真理と述定』、春秋社、2010",#090
'ana18'         :"戸田山和久   (著)、『知識の哲学』、産業図書、2002",#091
'sci8'          :"戸田山和久   (著)、『科学哲学の冒険    サイエンスの目的と方法をさぐる』、NHK出版、2005",#092
'ana15'         :"冨田恭彦    (著)、『アメリカ言語哲学の視点』、世界思想社、1996",#093
'sci4'          :"冨田恭彦    (著)、『哲学の最前線―ハーバードより愛をこめて』、講談社、1998",#094
'sci5'          :"冨田恭彦    (著)、『科学哲学者  柏木達彦の多忙な夏   科学がわかる哲学入門』、角川学芸出版、2009",#095
'sci6'          :"冨田恭彦    (著)、『科学哲学者  柏木達彦の春麗ら』、ナカニシヤ出版、2000",#096
'greek21'       :"富松保文    (著)、『アリストテレスはじめての形而上学』、NHK出版、2012",#097
'other1'        :"トルストイ   (著)・中村 融(翻訳)、『芸術とはなにか』、角川書店、1952",#098
'other91'       :"トルストイ   (著)・原卓也(翻訳)、『人生論』、新潮文庫、1975",#098
'ana24'         :"永井均 (著)、『ウィトゲンシュタイン入門』、筑摩書房、1995",#099
'med3'          :"中川純男ほか (編集)、『中世哲学を学ぶ人のために』、世界思想社、2005",#100
'de2'           :"中島義道   (著)、『カントの読み方』、筑摩書房、2008",#101
'indo1'         :"中村元    (著)、『龍樹』、講談社、2002",#102
'hist22'        :"西脇与作   (著)、『現代哲学入門』、慶應義塾大学出版会、2002",#103
'sci10'         :"西脇与作   (著)、『科学の哲学』、慶應義塾大学出版会、2004",#104
'phen5'         :"新田義弘   (編集)、『フッサールを学ぶ人のために』、世界思想社、2000",#105
'ana19'         :"新田義弘ほか (編集)、『岩波講座  現代思想〈7〉分析哲学とプラグマティズム』、岩波書店、1994",#106
'hist23'        :"貫成人    (著)、『図解雑学   哲学』、ナツメ社、2001",#107
'greek31'       :"納富信留   (著)、『ソフィストとは誰か?』、ちくま学芸文庫、2015",#108
'greek32'       :"納富信留   (著)、『プラトン   理想国の現在』、岩波新書、2012",#109
'hist24'        :"野家啓一   (編集)、『哲学の歴史〈10〉危機の時代の哲学』、中央公論新社、2008",#110
'ana13'         :"信原幸弘   (編集)、『シリーズ心の哲学〈2〉ロボット篇』、勁草書房、2004",#111
'ana26'         :"野本和幸   (著)、『現代の論理的意味論―フレーゲからクリプキまで』、岩波書店、1988",#112
'ana27'         :"野本和幸ほか (編集)、『言語哲学を学ぶ人のために』、世界思想社、2002",#113
'ana28'         :"野矢茂樹   (著)、『ウィトゲンシュタイン『論理哲学論考』を読む』、筑摩書房、2006",#114
'other5'        :"野矢茂樹   (著)、『哲学・航海日誌』、春秋社、1999",#115
'greek33'       :"荻野弘之   (著)、『哲学の饗宴―ソクラテス・プラトン・アリストテレス』、日本放送出版協会、2003",#116
'de1'           :"バウムガルトナー,       H.  M.  (著)・有福孝岳(翻訳)、『カント入門講義―『純粋理性批判』読解のために』、法政大学出版局、1994",#117
'greek8'        :"ハヴロック,      E.  A.  (著)・村岡晋一(翻訳)、『プラトン序説』、新書館、1997",#118
'fr13'          :"橋爪大三郎  (著)、『はじめての構造主義』、講談社、1988",#119
'ana20'         :"服部裕幸   (著)、『言語哲学入門』、勁草書房、2003",#120
'indo3'         :"早島鏡正   (著)、『インド思想史』、東京大学出版会、1982",#121
'hist9'         :"原佑ほか   (著)、『西洋哲学史』、東京大学出版会、1955",#122
'indo10'        :"針貝邦生   (著)、『ヴェーダからウパニシャッドへ (Century    Books―人と思想)』、清水書院、2000",#123
'exist4'        :"パルマー,       D.  D.  (著)・沢田  直(翻訳)、『サルトル』、筑摩書房、2003",#124
'fr14'          :"檜垣立哉   (著)、『ドゥルーズ入門』、筑摩書房、2009",#125
'modern3'       :"ヒューム,       D.  (著)・斎藤繁雄ほか(翻訳)、『人間知性研究―付・人間本性論摘要』、法政大学出版局、2011",#126
'hist5'         :"ヒルシュベルガー,   (著)・高橋憲一(翻訳)、『西洋哲学史〈1〉古代』、理想社、1967",#127
'hist6'         :"ヒルシュベルガー,   (著)・高橋憲一(翻訳)、『西洋哲学史〈2〉中世』、理想社、1970",#128
'hist7'         :"ヒルシュベルガー,   (著)・高橋憲一(翻訳)、『西洋哲学史〈3〉近代』、理想社、1976",#129
'hist8'         :"ヒルシュベルガー,   (著)・高橋憲一(翻訳)、『西洋哲学史〈4〉現代』、理想社、1978",#130
'greek26'       :"廣川洋一   (著)、『ソクラテス以前の哲学者』、講談社、1997",#131
'ana11'         :"フォン・ヴリグト,       G.  H.  (著)・服部裕幸    (監修)・牛尾光一(翻訳)、『論理分析哲学』、講談社、2000",#132
'de7'           :"福吉勝男   (著)、『フィヒテ   (Century    Books―人と思想)』、清水書院、1990",#133
'greek34'       :"藤沢令夫   (著)、『イデアと世界』、岩波書店、1999",#134
'greek35'       :"藤沢令夫   (著)、『プラトンの哲学』、岩波新書、1998",#135
'de8'           :"藤田昇吾   (著)、『カント哲学の特性』、晃洋書房、2004",#136
'fr17'          :"船木亨    (著)、『ドゥルーズ  (Century    Books―人と思想)』、清水書院、1994",#137
'greek9'        :"ブラック       R.  S.  (著)・内山勝利(翻訳)、『プラトン入門』、岩波書店、1992",#138
'greek10'       :"プラトン   (著)・生島幹三ほか  (翻訳)、『プラトン全集〈7〉 テアゲス    カルミデス   ラケス リュシス』、岩波書店、2005",#139
'greek11'       :"プラトン   (著)・藤沢令夫(翻訳).『メノン』、岩波文庫、1994",#140
'greek12'       :"プラトン   (著)・藤沢令夫(翻訳)、『国家〈上〉』、岩波文庫、1979年",#141
'greek13'       :"プラトン   (著)・藤沢令夫(翻訳)、『国家〈下〉』、岩波文庫、1979年",#142
'indo2'         :"前田専学   (著)、『インド哲学へのいざない    ヴェーダとウパニシャッド』、NHK出版、2000",#144
'de6'           :"町田健    (著)、『ソシュールと言語学』、講談社、2004",#145
'ana21'         :"末木剛博ほか (著)、『講座現代の哲学〈2〉分析哲学』、有斐閣、1958",#146
'exist6'        :"松浪信三郎  (著)、『サルトル』、勁草書房、1966",#147
'exist7'        :"松浪信三郎  (著)、『実存主義』、岩波書店、1962",#148
'phen1'         :"マルクス,       W.  (著)・佐藤真理人ほか(翻訳)、『フッサール現象学入門』、文化書房博文社、1994",#149
'hist26'        :"峰島旭雄   (著)、『概説 西洋哲学史』、ミネルヴァ書房、1989",#150
'fr11'          :"村上隆夫   (著)、『メルロ=ポンティ』、清水書院、1992",#151
'phen2'         :"メルロ=ポンティ,       M.  (著)・滝浦静雄ほか(翻訳)、『行動の構造』、みすず書房、1964",#152
'phen3'         :"メルロ=ポンティ,       M.  (著)・竹内芳郎ほか(翻訳)、『知覚の現象学  1』、みすず書房、1967",#153
'phen4'         :"メルロ=ポンティ,       M.  (著)・竹内芳郎ほか(翻訳)、『知覚の現象学  2』、みすず書房、1974",#154
'sci9'          :"森田邦久   (著)、『科学哲学講義』、筑摩書房、2012",#155
'ana23'         :"森本浩一   (著)、『デイヴィドソン　「言語」なんて存在するのだろうか』、NHK出版、2004",#156
'greek17'       :"八木雄二   (著)、『古代哲学への招待―パルメニデスとソクラテスから始めよう』、平凡社、2002",#157
'indo6'         :"矢島羊吉   (著)、『空の哲学』、日本放送出版協会、1983",#158
'hist14'        :"山内勝利   (編集)、『哲学の歴史〈2〉帝国と賢者』、中央公論新社、2007",#159
'hist13'        :"山内勝利   (編集)、『哲学の歴史〈1〉哲学誕生』、中央公論新社、2008",#160
'greek22'       :"山内勝利   (編集)、『ソクラテス以前哲学者断片集』、岩波書店、2008",#161
'greek23'       :"山口義久   (著)、『アリストテレス入門  』、筑摩書房、2001",#162
'greek24'       :"山口義久   (著)、『アリストテレス入門』、筑摩書房、2001",#163
'ana17'         :"山崎正一   (著)、『講座現代の哲学〈3〉プラグマティズム』、有斐閣、1958",#164
'fr4'           :"吉田禎吾ほか (著)、『レヴィ・ストロース  (Century    Books―人と思想)』、清水書院、1991",#165
'ana12'         :"ライカン,      W.  G.  (著)・荒磯敏文ほか(翻訳)、『言語哲学―入門から中級まで』、勁草書房、2005",#166
'other2'        :"ラコスト,      J.  (著)・阿部成樹(翻訳)、『芸術哲学入門    』、白水社、2002",#167
'hist3'         :"リーゼンフーバー,      K.  (著)・村井則夫(翻訳)、『西洋古代・中世哲学史』、平凡社、2000",#168
'modern4'       :"ルソー    (著)・今野一雄(翻訳)、『エミール〈上〉』、岩波書店、1962",#169
'modern44'      :"ルソー    (著)・今野一雄(翻訳)、要修正『人間不平等起源論』、岩波書店、1962",#169
'greek15'       :"ロメイエ=デルベ,      G.  (著)・神崎繁ほか(翻訳)、『ソフィスト列伝』、文庫クセジュ、2003",#170
'greek16'       :"ロング,       A.  A.  (著)・金山弥平(翻訳)、『ヘレニズム哲学-ストア派、エピクロス派、懐疑派』、京都大学学術出版会、2003",#171
'fr18'          :"鷲田清一   (著)、『メルロ=ポンティ―可逆性』、講談社、1997",#172
'other7'        :"渡辺二郎   (著)、『芸術の哲学』、筑摩書房、1998",#173
'add1'          :"ディオゲネス・ラエルティオス(著)・加来彰俊 (翻訳)、『ギリシア哲学者列伝（上）』、岩波書店、1984",
'add2'          :"ウィトゲンシュタイン(著)・野矢茂樹 (翻訳)、『論理哲学論考』、岩波文庫、2003",
}

app = flask.Flask(__name__)

# common_html = "http://127.0.0.1:5000"
common_html = "https://nomuras.github.io"

@app.route('/')
def index():
    return flask.render_template(
    	'index.html', 
        title=''
    	)

@app.route('/pages/')
def about():
    return flask.render_template(
        '/pages/about.html', 
        title='about'
        )

# @app.route('/pages/<page_num>.html', methods=['GET'])
# def trans_page(page_num):
#     return flask.render_template(
#         '/pages/'+page_num+'.html', 
#         page_num=page_num,
#         )


# ancient
@app.route('/pages/ancient/<page_num>.html', methods=['GET'])
def trans_ancient(page_num):
    return flask.render_template(
        '/pages/ancient/%s.html' % page_num, 
        title= '古代哲学',
        prev_page= common_html + "/pages/ancient/%s.html" % (int(page_num)-1),
        next_page= common_html + "/pages/ancient/%s.html" % (int(page_num)+1),
        reference=REFERENCE,
        )

# medieval
@app.route('/pages/medieval/<page_num>.html', methods=['GET'])
def trans_medieval(page_num):
    return flask.render_template(
    	'/pages/medieval/%s.html' % page_num, 
        title= '中世哲学',
        prev_page= common_html + "/pages/medieval/%s.html" % (int(page_num)-1),
        next_page= common_html + "/pages/medieval/%s.html" % (int(page_num)+1),
        reference=REFERENCE,
    	)
    
# modern
@app.route('/pages/modern/<page_num>.html', methods=['GET'])
def trans_modern(page_num):
    return flask.render_template(
        '/pages/modern/'+page_num+'.html', 
        title= '近代哲学',
        prev_page= common_html + "/pages/modern/%s.html" % (int(page_num)-1),
        next_page= common_html + "/pages/modern/%s.html" % (int(page_num)+1),
        reference=REFERENCE,
        )

# contemporary
@app.route('/pages/contemporary/<page_num>.html', methods=['GET'])
def trans_contemporary(page_num):
    return flask.render_template(
        '/pages/contemporary/'+page_num+'.html', 
        title= '現代哲学',
        prev_page= common_html + "/pages/contemporary/%s.html" % (int(page_num)-1),
        next_page= common_html + "/pages/contemporary/%s.html" % (int(page_num)+1),
        reference=REFERENCE,
        )

# phenomenology
@app.route('/pages/phenomenology/<page_num>.html', methods=['GET'])
def trans_phenomenology(page_num):
    return flask.render_template(
        '/pages/phenomenology/'+page_num+'.html', 
        title= '現象学',
        prev_page= common_html + "/pages/phenomenology/%s.html" % (int(page_num)-1),
        next_page= common_html + "/pages/phenomenology/%s.html" % (int(page_num)+1),
        reference=REFERENCE,
        )

# # existential
# @app.route('/pages/existential/<page_num>.html', methods=['GET'])
# def trans_existential(page_num):
#     return flask.render_template(
#         '/pages/existential/'+page_num+'.html', 
#         title= '実存主義',
#         prev_page= common_html + "/pages/existential/%s.html" % (int(page_num)-1),
#         next_page= common_html + "/pages/existential/%s.html" % (int(page_num)+1),
#         reference=REFERENCE,
#         )

# fr
@app.route('/pages/fr/<page_num>.html', methods=['GET'])
def trans_fr(page_num):
    return flask.render_template(
        '/pages/fr/'+page_num+'.html', 
        title= '現代フランス哲学',
        prev_page= common_html + "/pages/fr/%s.html" % (int(page_num)-1),
        next_page= common_html + "/pages/fr/%s.html" % (int(page_num)+1),
        reference=REFERENCE,
        )
    

# en
@app.route('/pages/en/<page_num>.html', methods=['GET'])
def trans_en(page_num):
    return flask.render_template(
        '/pages/en/'+page_num+'.html', 
        title= '現代イギリス哲学',
        prev_page= common_html + "/pages/en/%s.html" % (int(page_num)-1),
        next_page= common_html + "/pages/en/%s.html" % (int(page_num)+1),
        last_page= common_html + "/pages/en/15.html",
        reference=REFERENCE,
        )
    

# us
@app.route('/pages/us/<page_num>.html', methods=['GET'])
def trans_us(page_num):
    return flask.render_template(
        '/pages/us/'+page_num+'.html', 
        page_num=page_num,
        title= '現代アメリカ哲学',
        prev_page= common_html + "/pages/us/%s.html" % (int(page_num)-1),
        next_page= common_html + "/pages/us/%s.html" % (int(page_num)+1),
        reference=REFERENCE,
        )
    
# lang
@app.route('/pages/lang/<page_num>.html', methods=['GET'])
def trans_lang(page_num):
    return flask.render_template(
        '/pages/lang/'+page_num+'.html', 
        page_num=page_num,
        title= '言語哲学',
        prev_page= common_html + "/pages/lang/%s.html" % (int(page_num)-1),
        next_page= common_html + "/pages/lang/%s.html" % (int(page_num)+1),
        reference=REFERENCE,
        )
    
# science
@app.route('/pages/science/<page_num>.html', methods=['GET'])
def trans_science(page_num):
    return flask.render_template(
        '/pages/science/'+page_num+'.html', 
        title= '科学哲学',
        prev_page= common_html + "/pages/science/%s.html" % (int(page_num)-1),
        next_page= common_html + "/pages/science/%s.html" % (int(page_num)+1),
        reference=REFERENCE,
        )
    
# mind
@app.route('/pages/mind/<page_num>.html', methods=['GET'])
def trans_mind(page_num):
    return flask.render_template(
        '/pages/mind/'+page_num+'.html', 
        title= '心の哲学',
        prev_page= common_html + "/pages/mind/%s.html" % (int(page_num)-1),
        next_page= common_html + "/pages/mind/%s.html" % (int(page_num)+1),
        reference=REFERENCE,
        )
    
# epist
@app.route('/pages/epistemology/<page_num>.html', methods=['GET'])
def trans_epistemology(page_num):
    return flask.render_template(
        '/pages/epistemology/'+page_num+'.html', 
        title= '認識論',
        prev_page= common_html + "/pages/epistemology/%s.html" % (int(page_num)-1),
        next_page= common_html + "/pages/epistemology/%s.html" % (int(page_num)+1),
        reference=REFERENCE,
        )
    
# logic
@app.route('/pages/logic/<page_num>.html', methods=['GET'])
def trans_logic(page_num):
    return flask.render_template(
        '/pages/logic/'+page_num+'.html', 
        title= '論理学',
        prev_page= common_html + "/logic/medieval/%s.html" % (int(page_num)-1),
        next_page= common_html + "/logic/medieval/%s.html" % (int(page_num)+1),
        reference=REFERENCE,
        )
    
# east
@app.route('/pages/east/<page_num>.html', methods=['GET'])
def trans_east(page_num):
    return flask.render_template(
        '/pages/east/%s.html' % page_num, 
        title= '東洋哲学',
        prev_page= common_html + "/pages/east/%s.html" % (int(page_num)-1),
        next_page= common_html + "/pages/east/%s.html" % (int(page_num)+1),
        reference=REFERENCE,
        )

# others
@app.route('/pages/others/<page_num>.html', methods=['GET'])
def trans_others(page_num):
    return flask.render_template(
        '/pages/others/'+page_num+'.html', 
        title= 'others',
        prev_page= common_html + "/pages/others/%s.html" % (int(page_num)-1),
        next_page= common_html + "/pages/others/%s.html" % (int(page_num)+1),
        reference=REFERENCE,
        )
    
if __name__ == "__main__":
    app.run(debug=True)

