# Finding complete rewriting systems for 1-relation monoids

In
[Cirpons, Hivert, Mahboubi, Melquiond, Mitchell and Smith (2026)](https://doi.org/10.1145/3779031.3779101),
the authors present a toolbox for the
[Rocq proof assistant](https://rocq-prover.org/), that can be used to verify the
decidability of the word problem for a given monoid and, in some cases, to
produce the corresponding decision procedure. In particular, the techniques
described in this paper were applied to a large number of 1-relation monoids to
determine their decidability. Of these, 501 required a modified version of the
Knuth-Bendix procedure along with the termination solver `Matchbox` to find a
complete reqriting system, thus proving decidability.

On the following pages, you will find complete rewriting systems for 412 of
those 501 presentations. The complete rewriting systems described here were
found using the Knuth-Bendix procedure implemented in
[`libsemigroups`](https://libsemigroups.github.io/libsemigroups/), using the
morphocompletion technique as described in
[Pedersen (2005)](https://doi.org/10.1007/3-540-51081-8_141) and by Pestov in
[Slava's Monoid Zoo](https://monoids.net/).

## Hall of fame

The following information may be of particular interest.

### The presentations whose complete rewriting systems contains the most rules (128)

- [#309 baaaaababa=abbaa](309.md) (128 rules)
- [#394 baaaababa=abbaa](394.md) (87 rules)
- [#010 baaaaabbba=abaa](010.md) (87 rules)
- [#477 abbabbbaba=baabba](477.md) (87 rules)
- [#214 ababbaaaba=baaababa](214.md) (85 rules)
- [#332 abababaaaa=baaba](332.md) (82 rules)

### The presentations whose complete rewriting systems contains the fewest rules

- [#064 aaaabababa=babaaaaa](064.md) (3 rules)
- [#273 aaabababa=babaaaa](273.md) (3 rules)
- [#374 abaabababa=babaabaa](374.md) (3 rules)
- [#419 aababababa=babaaa](419.md) (3 rules)
- [#424 aababababa=bababaaa](424.md) (3 rules)
- [#462 abbaaababa=baabbaaa](462.md) (3 rules)

### The most common rules

Across all of the complete rewriting systems, there are $7,781$ rules in total,
and $6,572$ unique rules. There are $6,148$ rules that appear exactly once. The
following are the most common rules:

|    Rule     | Occurrences |
| :---------: | :---------: |
| $ba \to c$  |     131     |
| $c \to aa$  |     55      |
| $c \to ba$  |     29      |
| $bc \to cb$ |     26      |
| $abb \to d$ |     25      |
| $bb \to c$  |     25      |

## All presentations

### 000–049

|                                    |                                    |                                    |
| :--------------------------------- | :--------------------------------- | :--------------------------------- |
| [#000 ababbaaaaa=baaaaaba](000.md) | [#001 aabaababba=baaba](001.md)    | [#002 abbabbaaaa=babba](002.md)    |
| [#003 babbabaaba=abba](003.md)     | [#004 baabbaaaba=aabba](004.md)    | [#005 baaaaabbba=aaaaa](005.md)    |
| [#007 abaaabaaba=babaaa](007.md)   | [#008 aabaaaabba=baaabaa](008.md)  | [#010 baaaaabbba=abaa](010.md)     |
| [#011 babaaababa=aabababa](011.md) | [#012 bababbba=aba](012.md)        | [#013 ababaaabba=baaababa](013.md) |
| [#014 babbaababa=abba](014.md)     | [#015 baabaabbaa=abbaaba](015.md)  | [#016 baaaabbbaa=aaaa](016.md)     |
| [#017 aababbabba=babaa](017.md)    | [#018 aaabaaabba=baaabaa](018.md)  | [#020 aaabaabbaa=baaaba](020.md)   |
| [#021 aaaabaabba=baabaaa](021.md)  | [#023 baaabbbbba=aa](023.md)       | [#024 baaabaaaba=abbaa](024.md)    |
| [#025 abbababaaa=baabba](025.md)   | [#026 baaabaabaa=ababa](026.md)    | [#028 aaabababba=babaaa](028.md)   |
| [#029 abbabbaa=baba](029.md)       | [#030 baabbaabba=abababa](030.md)  | [#031 aaaabababa=babaa](031.md)    |
| [#032 baaabababa=abbaa](032.md)    | [#034 baaaabbbaa=abaaa](034.md)    | [#036 aababbaaaa=baaaaaba](036.md) |
| [#037 baaaabbbaa=aba](037.md)      | [#038 babaabbbba=abbbbaba](038.md) | [#040 baabbaabba=aa](040.md)       |
| [#042 baabababba=a](042.md)        | [#043 baaabbabba=aa](043.md)       | [#045 baabbaabaa=aabbaa](045.md)   |
| [#047 ababbababa=babababa](047.md) | [#048 abbababbba=baba](048.md)     | [#049 baabaabba=a](049.md)         |

### 050–099

|                                    |                                    |                                    |
| :--------------------------------- | :--------------------------------- | :--------------------------------- |
| [#050 babaabaaba=aabbabaa](050.md) | [#051 baaaaaabba=aaaaa](051.md)    | [#052 abaabbabba=babbaaba](052.md) |
| [#053 baaababbaa=abababa](053.md)  | [#054 bbaaabbaaa=abbaa](054.md)    | [#055 baabaabbba=aa](055.md)       |
| [#056 abbabbabaa=baba](056.md)     | [#057 abaabbbaba=babaa](057.md)    | [#058 baabbaaaba=abbaa](058.md)    |
| [#059 abbabbbaba=babba](059.md)    | [#060 baabbbabba=a](060.md)        | [#061 baaababbba=abaa](061.md)     |
| [#062 baabbbbba=aa](062.md)        | [#064 aaaabababa=babaaaaa](064.md) | [#066 abababbba=baba](066.md)      |
| [#067 baaaaabba=aabaa](067.md)     | [#068 baaaabbba=aa](068.md)        | [#069 abaabaabba=babaa](069.md)    |
| [#070 abababbaaa=baababa](070.md)  | [#071 baababbba=aba](071.md)       | [#072 baaaaabbba=aaa](072.md)      |
| [#074 abaababaa=baaba](074.md)     | [#075 baaababba=aba](075.md)       | [#076 baaaabbbba=aa](076.md)       |
| [#077 aabbabbaba=babaa](077.md)    | [#078 baaaabbbba=aaa](078.md)      | [#080 aaaababbaa=babaaa](080.md)   |
| [#081 aabaababba=baabaa](081.md)   | [#082 abbaaabbaa=babba](082.md)    | [#083 baabaabbaa=aabbaaba](083.md) |
| [#086 aaabbbaaba=baabbaa](086.md)  | [#088 bbaaabbbba=abbaa](088.md)    | [#089 baabbaabba=aba](089.md)      |
| [#091 abaaabbaba=babaa](091.md)    | [#092 abbaababba=bababbaa](092.md) | [#093 aabaaaabba=babaa](093.md)    |
| [#094 baaaabba=aa](094.md)         | [#095 babbabbbba=abba](095.md)     | [#096 baabaabbaa=abababa](096.md)  |
| [#097 baababbbaa=aaba](097.md)     | [#098 baaaabba=aaa](098.md)        |                                    |

### 100–149

|                                    |                                    |                                   |
| :--------------------------------- | :--------------------------------- | :-------------------------------- |
| [#100 aaabababaa=baaaaba](100.md)  | [#101 baaaaabbba=aaaa](101.md)     | [#102 baaabbaba=aa](102.md)       |
| [#103 abbabbaa=babba](103.md)      | [#104 babaaabbba=aba](104.md)      | [#107 baaaabbbba=aaaa](107.md)    |
| [#108 baabbabba=a](108.md)         | [#110 abbaababa=baabbaa](110.md)   | [#111 baabbabaa=aabba](111.md)    |
| [#112 baababba=aba](112.md)        | [#113 abbababbaa=babba](113.md)    | [#114 aababbabaa=babaaba](114.md) |
| [#115 bbaabbbbaa=aabba](115.md)    | [#116 abababaaba=bababaa](116.md)  | [#117 baaaaabbba=abaaa](117.md)   |
| [#118 ababaaaaba=baba](118.md)     | [#119 bbaabbaa=abba](119.md)       | [#121 baaaaaabba=aa](121.md)      |
| [#122 babaababaa=abaabba](122.md)  | [#123 baabbaaba=abbaa](123.md)     | [#124 bbaabbbbaa=aabbbba](124.md) |
| [#126 baaaababba=aaa](126.md)      | [#127 baaabbabaa=abaaabba](127.md) | [#128 aaaabbabba=babaa](128.md)   |
| [#129 baaaaabba=abaaaa](129.md)    | [#130 baaaaabbaa=aaa](130.md)      | [#131 babbaaabba=abbaa](131.md)   |
| [#132 baabaababa=abaabbaa](132.md) | [#133 bbbaabbbaa=abbba](133.md)    | [#134 baabbbba=aa](134.md)        |
| [#135 baabbba=aa](135.md)          | [#136 abaaababa=baaaba](136.md)    | [#137 abaabbbbba=babaa](137.md)   |
| [#138 aababbbaa=baaba](138.md)     | [#139 abababbaaa=baaba](139.md)    | [#140 abaaabaaba=baaaba](140.md)  |
| [#141 ababaaabba=baba](141.md)     | [#142 baabaaaaba=aabaaba](142.md)  | [#143 baaaabbbba=abaa](143.md)    |
| [#144 baaaaababa=abaaa](144.md)    | [#145 baababaaba=a](145.md)        | [#147 baaaaabbaa=aaaa](147.md)    |
| [#148 ababaabbba=baba](148.md)     | [#149 abaababaa=baabaa](149.md)    |                                   |

### 150–199

|                                    |                                    |                                    |
| :--------------------------------- | :--------------------------------- | :--------------------------------- |
| [#151 ababaababa=bababaa](151.md)  | [#152 babaaaabba=aaabbaba](152.md) | [#153 baaaababaa=abaaba](153.md)   |
| [#154 aababaabba=babaa](154.md)    | [#156 ababaabaaa=baba](156.md)     | [#157 bababaabba=ababa](157.md)    |
| [#160 baaabbabba=abbbaa](160.md)   | [#161 baaaababba=abaaa](161.md)    | [#163 aabbaababa=baaabbaa](163.md) |
| [#166 abbabaaaba=baba](166.md)     | [#168 baaabbbba=aa](168.md)        | [#169 abbaababaa=baaba](169.md)    |
| [#170 baaabbbaa=aaa](170.md)       | [#171 baaabbabaa=aaabba](171.md)   | [#172 baaabbbba=aaa](172.md)       |
| [#173 baabbabbba=a](173.md)        | [#174 ababaaaba=baba](174.md)      | [#175 baaabaabaa=aabba](175.md)    |
| [#176 bababbbba=aba](176.md)       | [#177 abbababbaa=bababa](177.md)   | [#179 babababbba=abbaba](179.md)   |
| [#180 babababbba=ababa](180.md)    | [#181 aabbaabaa=baaba](181.md)     | [#182 baaabbba=aa](182.md)         |
| [#183 abbabbabba=bbabbaa](183.md)  | [#184 abababbaba=bababa](184.md)   | [#185 baaabbba=aaa](185.md)        |
| [#186 baabaaaba=abaa](186.md)      | [#187 babbababa=abba](187.md)      | [#188 abbaaababa=baabbaa](188.md)  |
| [#189 ababaabbaa=baabaaba](189.md) | [#190 abaaabbaba=babaaa](190.md)   | [#191 baaaaaabba=aaaaaa](191.md)   |
| [#192 baaabbbbaa=aaa](192.md)      | [#194 baaabbaaba=aabbbaa](194.md)  | [#195 baabbababa=abbaba](195.md)   |
| [#196 babbababba=abbabba](196.md)  | [#198 baaaaabbaa=abaaaa](198.md)   | [#199 ababbababa=baaba](199.md)    |

### 200–249

|                                    |                                    |                                    |
| :--------------------------------- | :--------------------------------- | :--------------------------------- |
| [#200 ababaaabaa=baba](200.md)     | [#203 baabbabbaa=aba](203.md)      | [#204 aabaaababa=baabaa](204.md)   |
| [#205 baababbaa=aaba](205.md)      | [#206 abababbaa=baba](206.md)      | [#207 aababbaaaa=baaaaba](207.md)  |
| [#208 abbbabbbaa=babbba](208.md)   | [#209 abbaabbbaa=baabba](209.md)   | [#210 baaabbaaba=abbabaa](210.md)  |
| [#211 baaaabbba=aaa](211.md)       | [#213 abbaabbbba=babbaa](213.md)   | [#214 ababbaaaba=baaababa](214.md) |
| [#215 bababababa=ababbaba](215.md) | [#216 abbababbaa=bababba](216.md)  | [#217 babaaabba=ababa](217.md)     |
| [#218 abaababba=babaa](218.md)     | [#219 bababaaaba=aababa](219.md)   | [#220 baaabbaaba=abaa](220.md)     |
| [#221 aaababbaba=babaa](221.md)    | [#222 aabaaababa=babaaa](222.md)   | [#224 babababbba=aba](224.md)      |
| [#225 abbaabbaa=baba](225.md)      | [#226 aabaabbaaa=baaaba](226.md)   | [#227 baaaabbba=aaaa](227.md)      |
| [#229 abbabbabaa=bababba](229.md)  | [#231 abbaababba=babbaa](231.md)   | [#232 baaabbbbaa=aba](232.md)      |
| [#233 abaababaaa=baaabaa](233.md)  | [#234 baaababbaa=abbaaaba](234.md) | [#235 abaabababa=baaba](235.md)    |
| [#236 babaaaaaba=ababaa](236.md)   | [#237 ababbaba=bababa](237.md)     | [#238 baabaabaa=aabbaa](238.md)    |
| [#239 abaabaabba=baababaa](239.md) | [#242 abbabbbaaa=bababba](242.md)  | [#243 baaaabbbaa=a](243.md)        |
| [#244 baaaabba=aaaa](244.md)       | [#245 abaabaaba=babaa](245.md)     | [#247 abaaabbaaa=baaaaba](247.md)  |
| [#248 baaaaabbaa=a](248.md)        | [#249 baaaabaaaa=aaaaaba](249.md)  |                                    |

### 250–299

|                                    |                                    |                                    |
| :--------------------------------- | :--------------------------------- | :--------------------------------- |
| [#250 ababbbbaaa=baba](250.md)     | [#251 baabaabaa=ababa](251.md)     | [#252 baaaaaabba=aaa](252.md)      |
| [#255 baabababaa=abbaaba](255.md)  | [#256 ababbaabaa=baabaaba](256.md) | [#257 baaabbbaba=aa](257.md)       |
| [#258 aabbaabbaa=baabba](258.md)   | [#259 bababbbaba=ababbba](259.md)  | [#260 baaabbaa=abaaa](260.md)      |
| [#262 baabaaabba=aabaa](262.md)    | [#263 aabaabaaba=baabaa](263.md)   | [#264 abaabbaaba=baaba](264.md)    |
| [#265 baaaabbaba=aa](265.md)       | [#266 ababbabbaa=baba](266.md)     | [#267 ababbabbba=babbbaba](267.md) |
| [#268 aababaabaa=baaba](268.md)    | [#269 baaaaaabba=aaaa](269.md)     | [#270 baaaabbaba=aaa](270.md)      |
| [#271 baaaaabbba=abbaa](271.md)    | [#272 ababababa=babaaba](272.md)   | [#273 aaabababa=babaaaa](273.md)   |
| [#275 baaabba=aa](275.md)          | [#276 aabaababaa=baaba](276.md)    | [#277 baaaababaa=aaaba](277.md)    |
| [#278 baababbba=a](278.md)         | [#279 abbabaa=baba](279.md)        | [#280 abaabbabaa=babaaaba](280.md) |
| [#282 abababaaba=babaa](282.md)    | [#283 baabbbaaba=aabbbaa](283.md)  | [#285 baaabaaaba=aaabba](285.md)   |
| [#286 bababaaaba=aabababa](286.md) | [#288 abbaabbaa=babba](288.md)     | [#289 abbabbbaba=bababba](289.md)  |
| [#290 abaabbaa=baaba](290.md)      | [#291 baabbabbaa=aabba](291.md)    | [#292 baaaaabba=aa](292.md)        |
| [#293 babaaaabba=ababa](293.md)    | [#294 babbaaba=abba](294.md)       | [#296 ababbbabba=babbaba](296.md)  |
| [#297 baabaabba=aa](297.md)        | [#299 babaababba=ababbaba](299.md) |                                    |

### 300–349

|                                    |                                   |                                    |
| :--------------------------------- | :-------------------------------- | :--------------------------------- |
| [#300 aabbaabbba=baabba](300.md)   | [#301 abaabababa=babaaba](301.md) | [#302 babaabbbba=aba](302.md)      |
| [#303 abbababaa=baabba](303.md)    | [#305 baaaabbaa=abaaa](305.md)    | [#306 aabababbaa=baaba](306.md)    |
| [#307 baabbbbbba=aa](307.md)       | [#308 baabbaa=aabba](308.md)      | [#309 baaaaababa=abbaa](309.md)    |
| [#310 babaababa=abababa](310.md)   | [#312 baaaabbaba=abaaa](312.md)   | [#313 abaabbaaaa=baaaba](313.md)   |
| [#315 aaaabbaaba=baabaaa](315.md)  | [#317 bababbaaba=ababba](317.md)  | [#318 baababba=a](318.md)          |
| [#321 baabbaabaa=abaabbaa](321.md) | [#322 abaabaaba=baabaa](322.md)   | [#323 aaaaababba=babaaaa](323.md)  |
| [#324 baabaaba=aabba](324.md)      | [#325 abaaaababa=baaabaa](325.md) | [#326 baaaabbaaa=aaaabbaa](326.md) |
| [#327 abaabbaba=babaa](327.md)     | [#328 abbabbbba=babba](328.md)    | [#329 babaaabbba=aabbbaba](329.md) |
| [#330 abaaababba=babaa](330.md)    | [#331 abaabaaaba=baaba](331.md)   | [#332 abababaaaa=baaba](332.md)    |
| [#333 aababababa=babaa](333.md)    | [#334 abbabbbaaa=baaabba](334.md) | [#335 baaabbbaba=abaa](335.md)     |
| [#336 baababbbaa=abba](336.md)     | [#337 baaaabbaa=abaaaa](337.md)   | [#338 abaabaaaba=babaa](338.md)    |
| [#339 aaabaaabba=baaaba](339.md)   | [#340 baabababaa=aaaba](340.md)   | [#342 babaababba=ababa](342.md)    |
| [#344 babbbabba=abbba](344.md)     | [#346 baababbaa=abaaba](346.md)   | [#347 ababbbabba=baba](347.md)     |
| [#348 baaaabbaba=abaa](348.md)     |                                   |                                    |

### 350–399

|                                    |                                   |                                    |
| :--------------------------------- | :-------------------------------- | :--------------------------------- |
| [#350 aaaabaabba=babaa](350.md)    | [#352 baabaaaba=abaaba](352.md)   | [#353 abaabbabaa=baaba](353.md)    |
| [#354 baabbaaaba=aabbaa](354.md)   | [#355 baaabbaba=a](355.md)        | [#356 baabaabaa=ababaa](356.md)    |
| [#357 abbabbaaa=babba](357.md)     | [#358 baaabbabaa=aabba](358.md)   | [#359 ababaaabaa=baaba](359.md)    |
| [#360 baabaabaa=abaaba](360.md)    | [#361 baaaabaaba=a](361.md)       | [#362 abbaabbaba=bababbaa](362.md) |
| [#363 aabaabbaba=babaaba](363.md)  | [#364 aabaababaa=baabaa](364.md)  | [#365 abaababbaa=baaba](365.md)    |
| [#366 aaababaaba=babaa](366.md)    | [#367 baaababaaa=abaaaba](367.md) | [#368 aababbbaba=babbaa](368.md)   |
| [#369 ababbabbaa=babbaaba](369.md) | [#370 baaababaaa=aababaa](370.md) | [#372 abbabbaaba=babba](372.md)    |
| [#374 abaabababa=babaabaa](374.md) | [#375 baabaabba=abaa](375.md)     | [#376 abaabababa=babaa](376.md)    |
| [#377 babaababaa=ababa](377.md)    | [#378 baabaaaba=aaabbaa](378.md)  | [#379 baaaabaaba=aabaa](379.md)    |
| [#381 babbaaaba=ababba](381.md)    | [#382 aaabbababa=babaaa](382.md)  | [#383 bababbbbba=aba](383.md)      |
| [#384 abaabaaaba=baabaaa](384.md)  | [#385 bbaaabbbba=aa](385.md)      | [#386 baabaaabaa=aba](386.md)      |
| [#388 babaabaaba=aabbaba](388.md)  | [#389 baaababaa=aababa](389.md)   | [#390 abaaabbaba=babaaaba](390.md) |
| [#391 bababaaba=ababa](391.md)     | [#392 baababbaba=a](392.md)       | [#393 babaaaabba=ababaa](393.md)   |
| [#394 baaaababa=abbaa](394.md)     | [#395 baaababba=aa](395.md)       | [#396 abaaaababa=babaa](396.md)    |
| [#397 abbabbbbaa=bbaabba](397.md)  | [#399 ababaaabba=babaaa](399.md)  |                                    |

### 400–449

|                                    |                                    |                                    |
| :--------------------------------- | :--------------------------------- | :--------------------------------- |
| [#400 baaaabbaaa=a](400.md)        | [#403 babaaaaaba=aaaababa](403.md) | [#404 abaaabaaba=babaa](404.md)    |
| [#405 aabaabbaaa=baaabaa](405.md)  | [#407 abbabbabaa=baabba](407.md)   | [#408 babaababaa=aba](408.md)      |
| [#409 aaababbaaa=baaaba](409.md)   | [#410 baaaaaabba=abaaaaa](410.md)  | [#411 aabaabbaba=babaabaa](411.md) |
| [#412 abaababbaa=baabaaba](412.md) | [#413 ababaabbaa=baababa](413.md)  | [#415 bbabaaabba=abbabaa](415.md)  |
| [#416 baaaababaa=aa](416.md)       | [#417 baaababbaa=aaaba](417.md)    | [#418 abaababbaa=babaaba](418.md)  |
| [#419 aababababa=babaaa](419.md)   | [#421 abaababa=baaba](421.md)      | [#422 aabbbaaba=baabbaa](422.md)   |
| [#423 baaaaabbaa=abaaaaa](423.md)  | [#424 aababababa=bababaaa](424.md) | [#426 bababaaaba=ababa](426.md)    |
| [#427 aaabababba=babaa](427.md)    | [#428 aabbaabbaa=baaba](428.md)    | [#429 baaaaabba=aaa](429.md)       |
| [#430 baabaabba=ababa](430.md)     | [#431 abababbaba=babababa](431.md) | [#432 baaabbbaaa=aba](432.md)      |
| [#433 baaaabaaba=abbaa](433.md)    | [#434 ababaaaba=babaaa](434.md)    | [#436 baabaaaaba=abaa](436.md)     |
| [#437 baaaaabbba=aa](437.md)       | [#438 baabbababa=abbaabba](438.md) | [#439 baaaabbaaa=aaaabba](439.md)  |
| [#440 ababbabba=baba](440.md)      | [#441 abaabbaaaa=baaba](441.md)    | [#444 abbababaa=bababa](444.md)    |
| [#445 abaaaababa=baabaaa](445.md)  | [#446 baaaaabba=aaaa](446.md)      | [#447 baaababa=a](447.md)          |
| [#448 baabaaabba=abaabaa](448.md)  |                                    |                                    |

### 450–501

|                                    |                                    |                                    |
| :--------------------------------- | :--------------------------------- | :--------------------------------- |
| [#450 baabababaa=aabbaaba](450.md) | [#451 baaabaaba=a](451.md)         | [#452 baabaabbaa=aaaba](452.md)    |
| [#453 aabbababaa=baaabba](453.md)  | [#454 ababababaa=babaa](454.md)    | [#457 ababaabbaa=baaababa](457.md) |
| [#458 baaabbbaa=aaabbba](458.md)   | [#459 baaabaaaba=aabaa](459.md)    | [#460 aabbaaabba=baabbaa](460.md)  |
| [#461 baaaababaa=abaaa](461.md)    | [#462 abbaaababa=baabbaaa](462.md) | [#463 baabababba=aba](463.md)      |
| [#465 abbaababaa=baababa](465.md)  | [#468 baabbbbbaa=aba](468.md)      | [#470 ababbabaa=baba](470.md)      |
| [#471 abaaababa=baabaa](471.md)    | [#472 baababbbaa=abbabba](472.md)  | [#473 abaabaaba=baaaba](473.md)    |
| [#474 bbaaabbaa=abba](474.md)      | [#475 baaabbaaba=abbaa](475.md)    | [#476 abababbaaa=baaababa](476.md) |
| [#477 abbabbbaba=baabba](477.md)   | [#478 babbabbaba=abbabba](478.md)  | [#479 bbaabbabba=a](479.md)        |
| [#481 babbabbbba=abbba](481.md)    | [#482 aabaaabbaa=baaaba](482.md)   | [#483 aabaabbaaa=baaba](483.md)    |
| [#484 ababbabaaa=baaba](484.md)    | [#485 baaaababba=aa](485.md)       | [#487 abbaabbaba=babbaa](487.md)   |
| [#488 baababaaba=aababbaa](488.md) | [#490 babaabaaba=ababa](490.md)    | [#491 baabaabbba=abaa](491.md)     |
| [#493 ababbbabba=bbabbaba](493.md) | [#494 baaaabbbaa=aaa](494.md)      | [#495 aababbaba=babaa](495.md)     |
| [#496 abaaaababa=babaaa](496.md)   | [#497 aabaabbaaa=baaaaba](497.md)  | [#498 bbaaabbaaa=aabba](498.md)    |
| [#499 baaaaaabba=aaabaa](499.md)   | [#500 abbbababaa=baabbba](500.md)  | [#501 baaaabbbaa=aaaabbba](501.md) |
