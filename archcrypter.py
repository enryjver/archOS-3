import random
replit.clear()
chars = ['૱', '꠸', '┯', '┰', '┱', '┲', '►', '◄', 'Ă', 'ă', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Ǖ', 'ǖ', 'Ꞁ', '¤', 'Ð', '¢', '℥', 'Ω', '℧', 'K', 'ℶ', 'ℷ', 'ℸ', 'ⅇ', '⅊', '⚌', '⚍', '⚎', '⚏', '⚭', '⚮', '⌀', '⏑', '⏒', '⏓', '⏔', '⏕', '⏖', '⏗', '⏘', '⏙', '⏠', '⏡', '⏦', 'ᶀ', 'ᶁ', 'ᶂ', 'ᶃ', 'ᶄ', 'ᶆ', 'ᶇ', 'ᶈ', 'ᶉ', 'ᶊ', 'ᶋ', 'ᶌ', 'ᶍ', 'ᶎ', 'ᶏ', 'ᶐ', 'ᶑ', 'ᶒ', 'ᶓ', 'ᶔ', 'ᶕ', 'ᶖ', 'ᶗ', 'ᶘ', 'ᶙ', 'ᶚ', 'ᶸ', 'ᵯ', 'ᵰ', 'ᵴ', 'ᵶ', 'ᵹ', 'ᵼ', 'ᵽ', 'ᵾ', 'ᵿ', '⁁', '⁊', '⸜', '⸝', '¶', '¥', '£', '⅕', '⅙', '⅛', '⅔', '⅖', '⅗', '⅘', '⅜', '⅚', '⅐', '⅝', '↉', '⅓', '⅑', '⅒', '⅞', '←', '↑', '→', '↓', '↔', '↕', '↖', '↗', '↘', '↙', '↚', '↛', '↜', '↝', '↞', '↟', '↠', '↡', '↢', '↣', '↤', '↥', '↦', '↧', '↨', '↩', '↪', '↫', '↬', '↭', '↮', '↯', '↰', '↱', '↲', '↳', '↴', '↵', '↶', '↷', '↸', '↹', '↺', '↻', '↼', '↽', '↾', '↿', '⇀', '⇁', '⇂', '⇃', '⇄', '⇅', '⇆', '⇇', '⇈', '⇉', '⇊', '⇋', '⇌', '⇍', '⇎', '⇏', '⇐', '⇑', '⇒', '⇓', '⇔', '⇕', '⇖', '⇗', '⇘', '⇙', '⇚', '⇛', '⇜', '⇝', '⇞', '⇟', '⇠', '⇡', '⇢', '⇣', '⇤', '⇥', '⇦', '⇨', '⇩', '⇪', '⇧', '⇫', '⇬', '⇭', '⇮', '⇯', '⇰', '⇱', '⇲', '⇳', '⇴', '⇵', '⇶', '⇷', '⇸', '⇹', '⇺', '⇻', '⇼', '⇽', '⇾', '⇿', '⟰', '⟱', '⟲', '⟳', '⟴', '⟵', '⟶', '⟷', '⟸', '⟹', '⟺', '⟻', '⟼', '⟽', '⟾', '⟿', '⤀', '⤁', '⤂', '⤃', '⤄', '⤅', '⤆', '⤇', '⤈', '⤉', '⤊', '⤋', '⤌', '⤍', '⤎', '⤏', '⤐', '⤑', '⤒', '⤓', '⤔', '⤕', '⤖', '⤗', '⤘', '⤙', '⤚', '⤛', '⤜', '⤝', '⤞', '⤟', '⤠', '⤡', '⤢', '⤣', '⤤', '⤥', '⤦', '⤧', '⤨', '⤩', '⤪', '⤫', '⤬', '⤭', '⤮', '⤯', '⤰', '⤱', '⤲', '⤳', '⤴', '⤵', '⤶', '⤷', '⤸', '⤹', '⤺', '⤻', '⤼', '⤽', '⤾', '⤿', '⥀', '⥁', '⥂', '⥃', '⥄', '⥅', '⥆', '⥇', '⥈', '⥉', '⥊', '⥋', '⥌', '⥍', '⥎', '⥏', '⥐', '⥑', '⥒', '⥓', '⥔', '⥕', '⥖', '⥗', '⥘', '⥙', '⥚', '⥛', '⥜', '⥝', '⥞', '⥟', '⥠', '⥡', '⥢', '⥣', '⥤', '⥥', '⥦', '⥧', '⥨', '⥩', '⥪', '⥫', '⥬', '⥭', '⥮', '⥯', '⥰', '⥱', '⥲', '⥳', '⥴', '⥵', '⥶', '⥷', '⥸', '⥹', '⥺', '⥻', '⥼', '⥽', '⥾', '⥿', '➔', '➘', '➙', '➚', '➛', '➜', '➝', '➞', '➝', '➞', '➟', '➠', '➡', '➢', '➣', '➤', '➥', '➦', '➧', '➨', '➩', '➩', '➪', '➫', '➬', '➭', '➮', '➯', '➱', '➲', '➳', '➴', '➵', '➶', '➷', '➸', '➹', '➺', '➻', '➼', '➽', '➾', '⬀', '⬁', '⬂', '⬃', '⬄', '⬅', '⬆', '⬇', '⬈', '⬉', '⬊', '⬋', '⬌', '⬍', '⬎', '⬏', '⬐', '⬑', '☇', '☈', '⏎', '⍃', '⍄', '⍅', '⍆', '⍇', '⍈', '⍐', '⍗', '⍌', '⍓', '⍍', '⍔', '⍏', '⍖', '♾', '⎌', '☊', '☋', '☌', '☍', '⌃', '⌄', '⌤', '⌅', '⌆', '⌇', '⚋', '⚊', '⌌', '⌍', '⌎', '⌏', '⌐', '⌑', '⌔', '⌕', '⌗', '⌙', '⌢', '⌣', '⌯', '⌬', '⌭', '⌮', '⌖', '⌰', '⌱', '⌲', '⌳', '⌴', '⌵', '⌶', '⌷', '⌸', '⌹', '⌺', '⌻', '⌼', '⍯', '⍰', '⌽', '⌾', '⌿', '⍀', '⍁', '⍂', '⍉', '⍊', '⍋', '⍎', '⍏', '⍑', '⍒', '⍕', '⍖', '⍘', '⍙', '⍚', '⍛', '⍜', '⍝', '⍞', '⍠', '⍟', '⍡', '⍢', '⍣', '⍤', '⍥', '⍨', '⍩', '⍦', '⍧', '⍬', '⍿', '⍪', '⍮', '⍫', '⍱', '⍲', '⍭', '⍳', '⍴', '⍵', '⍶', '⍷', '⍸', '⍹', '⍺', '⍼', '⍽', '⍾', '⎀', '⎁', '⎂', '⎃', '⎄', '⎅', '⎆', '⎉', '⎊', '⎋', '⎍', '⎎', '⎏', '⎐', '⎑', '⎒', '⎓', '⎔', '⎕', '⏣', '⌓', '⏥', '⏢', '⎖', '⎲', '⎳', '⎴', '⎵', '⎶', '⎸', '⎹', '⎺', '⎻', '⎼', '⎽', '⎾', '⎿', '⏀', '⏁', '⏂', '⏃', '⏄', '⏅', '⏆', '⏇', '⏈', '⏉', '⏉', '⏋', '⏌', '⏍', '⏐', '⏤', '⏚', '⏛', 'Ⓝ', 'ℰ', 'ⓦ', '!', '⌘', '«', '»', '‹', '›', '‘', '’', '“', '”', '„', '‚', '❝', '❞', '£', '¥', '€', '$', '¢', '¬', '¶', '@', '§', '®', '©', '™', '°', '×', 'π', '±', '√', '‰', 'Ω', '∞', '≈', '÷', '~', '≠', '¹', '²', '³', '½', '¼', '¾', '‐', '–', '—', '|', '⁄', '\\', '[', ']', '{', '}', '†', '‡', '…', '·', '•', '●', '⇧', '↩', '¡', '¿', '‽', '⁂', '∴', '∵', '◊', '※', '←', '→', '↑', '↓', '☼', '☺', '♠', '♦', '♣', '♥', '♪', '♫', '♯', '♀', '♂', 'α', 'ß', 'Á', 'á', 'À', 'à', 'Å', 'å', 'Ä', 'ä', 'Æ', 'æ', 'Ç', 'ç', 'É', 'é', 'È', 'è', 'Ê', 'ê', 'Í', 'í', 'Ì', 'ì', 'Î', 'î', 'Ñ', 'ñ', 'Ó', 'ó', 'Ò', 'ò', 'Ô', 'ô', 'Ö', 'ö', 'Ø', 'ø', 'Ú', 'ú', 'Ù', 'ù', 'Ü', 'ü', 'Ž', 'ž', '₳', '฿', '￠', '€', '₡', '¢', '₢', '₵', '₫', '￡', '£', '₤', '₣', 'ƒ', '₲', '₭', '₥', '₦', '₱', '＄', '$', '₮', '₩', '￦', '¥', '￥', '₴', '₰', '¤', '៛', '₪', '₯', '₠', '₧', '₨', '௹', '﷼', '㍐', '৲', '৳', '~', 'ƻ', 'Ƽ', 'ƽ', '¹', '¸', '¬', '¨', 'ɂ', 'ǁ', '¯', 'Ɂ', 'ǂ', '¡', '°', 'ꟾ', '¦', '}', '{', '|', '.', ',', '·', ']', ')', '[', '/', '_', '\\', '¿', 'º', '§', '*', '-', '+', '(', '!', '&', '%', '$', '¼', '¾', '½', '¶', '©', '®', '@', 'ẟ', 'Ɀ', '`', 'Ȿ', '^', '꜠', '꜡', 'ỻ', '=', ':', ';', '<', 'ꞌ', 'Ꞌ', '꞊', 'ꞁ', 'ꞈ', '꞉', '>', '?', '÷', 'ℾ', 'ℿ', '℔', '℩', '℉', '⅀', '℈', 'þ', 'ð', 'Þ', 'µ', 'ª', 'ꝋ', 'ꜿ', 'Ꜿ', 'ⱽ', 'ⱺ', 'ⱹ', 'ⱷ', 'ⱶ', 'Ⱶ', 'ⱴ', 'ⱱ', 'Ɒ', 'ⱦ', 'ȶ', 'ȴ', 'ȣ', 'Ȣ', 'ȡ', 'ȝ', 'Ȝ', 'ț', 'ȋ', 'Ȋ', 'ȉ', 'Ȉ', 'ǯ', 'Ǯ', 'ǃ', 'ǀ', 'ƿ', 'ƾ', 'ƺ', 'ƹ', 'Ƹ', 'Ʒ', 'Ʋ', 'ư', 'ƪ', 'ƣ', 'Ƣ', 'Ɵ', 'ƛ', 'Ɩ', 'ƕ', 'ƍ', 'ſ', 'ỽ', '⸀', '⸁', '⸂', '⸃', '⸄', '⸅', '⸆', '⸇', '⸈', '⸉', '⸊', '⸋', '⸌', '⸍', '⸎', '⸏', '⸐', '⸑', '⸒', '⸔', '⸕', '▲', '▼', '◀', '▶', '◢', '◣', '◥', '◤', '△', '▽', '◿', '◺', '◹', '◸', '▴', '▾', '◂', '▸', '▵', '▿', '◃', '▹', '◁', '▷', '◅', '▻', '◬', '⟁', '⧋', '⧊', '⊿', '∆', '∇', '◭', '◮', '⧩', '⧨', '⌔', '⟐', '◇', '◆', '◈', '⬖', '⬗', '⬘', '⬙', '⬠', '⬡', '⎔', '⋄', '◊', '⧫', '⬢', '⬣', '▰', '▪', '◼', '▮', '◾', '▗', '▖', '■', '∎', '▃', '▄', '▅', '▆', '▇', '█', '▌', '▐', '▍', '▎', '▉', '▊', '▋', '❘', '❙', '❚', '▀', '▘', '▝', '▙', '▚', '▛', '▜', '▟', '▞', '░', '▒', '▓', '▂', '▁', '▬', '▔', '▫', '▯', '▭', '▱', '◽', '□', '◻', '▢', '⊞', '⊡', '⊟', '⊠', '▣', '▤', '▥', '▦', '⬚', '▧', '▨', '▩', '⬓', '◧', '⬒', '◨', '◩', '◪', '⬔', '⬕', '❏', '❐', '❑', '❒', '⧈', '◰', '◱', '◳', '◲', '◫', '⧇', '⧅', '⧄', '⍁', '⍂', '⟡', '⧉', '⚬', '○', '◌', '◍', '◎', '◯', '❍', '◉', '⦾', '⊙', '⦿', '⊜', '⊖', '⊘', '⊚', '⊛', '⊝', '●', '⦁', '◐', '◑', '◒', '◓', '◔', '◕', '⦶', '⦸', '◵', '◴', '◶', '◷', '⊕', '⊗', '⦇', '⦈', '⦉', '⦊', '❨', '❩', '⸨', '⸩', '◖', '◗', '❪', '❫', '❮', '❯', '❬', '❭', '❰', '❱', '⊏', '⊐', '⊑', '⊒', '◘', '◙', '◚', '◛', '◜', '◝', '◞', '◟', '◠', '◡', '⋒', '⋓', '⋐', '⋑', '╰', '╮', '╭', '╯', '⌒', '╳', '✕', '╱', '╲', '⧸', '⧹', '⌓', '◦', '❖', '✖', '✚', '✜', '⧓', '⧗', '⧑', '⧒', '⧖', '_', '⚊', '╴', '╼', '╾', '‐', '⁃', '‑', '‒', '-', '–', '⎯', '—', '―', '╶', '╺', '╸', '─', '━', '┄', '┅', '┈', '┉', '╌', '╍', '═', '≣', '≡', '☰', '☱', '☲', '☳', '☴', '☵', '☶', '☷', '╵', '╷', '╹', '╻', '│', '▕', '▏', '┃', '┆', '┇', '┊', '╎', '┋', '╿', '╽', '┌', '┍', '┎', '┏', '┐', '┑', '┒', '┓', '└', '┕', '┖', '┗', '┘', '┙', '┚', '┛', '├', '┝', '┞', '┟', '┠', '┡', '┢', '┣', '┤', '┥', '┦', '┧', '┨', '┩', '┪', '┫', '┬', '┭', '┮', '┳', '┴', '┵', '┶', '┷', '┸', '┹', '┺', '┻', '┼', '┽', '┾', '┿', '╀', '╁', '╂', '╃', '╄', '╅', '╆', '╇', '╈', '╉', '╊', '╋', '╏', '║', '╔', '╒', '╓', '╕', '╖', '╗', '╚', '╘', '╙', '╛', '╜', '╝', '╞', '╟', '╠', '╡', '╢', '╣', '╤', '╥', '╦', '╧', '╨', '╩', '╪', '╫', '╬', '⌞', '⌟', '⌜', '⌝', '⌊', '⌋', '⌉', '⌈', '⌋', '₯', 'ἀ', 'ἁ', 'ἂ', 'ἃ', 'ἄ', 'ἅ', 'ἆ', 'ἇ', 'Ἀ', 'Ἁ', 'Ἂ', 'Ἃ', 'Ἄ', 'Ἅ', 'Ἆ', 'Ἇ', 'ἐ', 'ἑ', 'ἒ', 'ἓ', 'ἔ', 'ἕ', 'Ἐ', 'Ἑ', 'Ἒ', 'Ἓ', 'Ἔ', 'Ἕ', 'ἠ', 'ἡ', 'ἢ', 'ἣ', 'ἤ', 'ἥ', 'ἦ', 'ἧ', 'Ἠ', 'Ἡ', 'Ἢ', 'Ἣ', 'Ἤ', 'Ἥ', 'Ἦ', 'Ἧ', 'ἰ', 'ἱ', 'ἲ', 'ἳ', 'ἴ', 'ἵ', 'ἶ', 'ἷ', 'Ἰ', 'Ἱ', 'Ἲ', 'Ἳ', 'Ἴ', 'Ἵ', 'Ἶ', 'Ἷ', 'ὀ', 'ὁ', 'ὂ', 'ὃ', 'ὄ', 'ὅ', 'Ὀ', 'Ὁ', 'Ὂ', 'Ὃ', 'Ὄ', 'Ὅ', 'ὐ', 'ὑ', 'ὒ', 'ὓ', 'ὔ', 'ὕ', 'ὖ', 'ὗ', 'Ὑ', 'Ὓ', 'Ὕ', 'Ὗ', 'ὠ', 'ὡ', 'ὢ', 'ὣ', 'ὤ', 'ὥ', 'ὦ', 'ὧ', 'Ὠ', 'Ὡ', 'Ὢ', 'Ὣ', 'Ὤ', 'Ὥ', 'Ὦ', 'Ὧ', 'ὰ', 'ά', 'ὲ', 'έ', 'ὴ', 'ή', 'ὶ', 'ί', 'ὸ', 'ό', 'ὺ', 'ύ', 'ὼ', 'ώ', 'ᾀ', 'ᾁ', 'ᾂ', 'ᾃ', 'ᾄ', 'ᾅ', 'ᾆ', 'ᾇ', 'ᾈ', 'ᾉ', 'ᾊ', 'ᾋ', 'ᾌ', 'ᾍ', 'ᾎ', 'ᾏ', 'ᾐ', 'ᾑ', 'ᾒ', 'ᾓ', 'ᾔ', 'ᾕ', 'ᾖ', 'ᾗ', 'ᾘ', 'ᾙ', 'ᾚ', 'ᾛ', 'ᾜ', 'ᾝ', 'ᾞ', 'ᾟ', 'ᾠ', 'ᾡ', 'ᾢ', 'ᾣ', 'ᾤ', 'ᾥ', 'ᾦ', 'ᾧ', 'ᾨ', 'ᾩ', 'ᾪ', 'ᾫ', 'ᾬ', 'ᾭ', 'ᾮ', 'ᾯ', 'ᾰ', 'ᾱ', 'ᾲ', 'ᾳ', 'ᾴ', 'ᾶ', 'ᾷ', 'Ᾰ', 'Ᾱ', 'Ὰ', 'Ά', 'ᾼ', '᾽', 'ι', '᾿', '῀', '῁', 'ῂ', 'ῃ', 'ῄ', 'ῆ', 'ῇ', 'Ὲ', 'Έ', 'Ὴ', 'Ή', 'ῌ', '῍', '῎', '῏', 'ῐ', 'ῑ', 'ῒ', 'ΐ', '��', 'ῗ', 'Ῐ', 'Ῑ', 'Ὶ', 'Ί', '῝', '῞', '῟', 'ῠ', 'ῡ', 'ῢ', 'ΰ', 'ῤ', 'ῥ', 'ῦ', 'ῧ', 'Ῠ', 'Ῡ', 'Ὺ', 'Ύ', 'Ῥ', '῭', '΅', '`', 'ῲ', 'ῳ', 'ῴ', 'ῶ', 'ῷ', 'Ὸ', 'Ό', 'Ὼ', 'Ώ', 'ῼ', '´', '῾', 'Ͱ', 'ͱ', 'Ͳ', 'ͳ', 'ʹ', '͵', 'Ͷ', 'ͷ', 'ͺ', 'ͻ', 'ͼ', 'ͽ', ';', '΄', '΅', 'Ά', '·', 'Έ', 'Ή', 'Ί', 'Ό', 'Ύ', 'Ώ', 'ΐ', 'Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω', 'Ϊ', 'Ϋ', 'ά', 'έ', 'ή', 'ί', 'ΰ', 'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'ς', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω', 'ϊ', 'ϋ', 'ό', 'ύ', 'ώ', 'ϐ', 'ϑ', 'ϒ', 'ϓ', 'ϔ', 'ϕ', 'ϖ', 'ϗ', 'Ϙ', 'ϙ', 'Ϛ', 'ϛ', 'Ϝ', 'ϝ', 'Ϟ', 'ϟ', 'Ϡ', 'ϡ', 'Ϣ', 'ϣ', 'Ϥ', 'ϥ', 'Ϧ', 'ϧ', 'Ϩ', 'ϩ', 'Ϫ', 'ϫ', 'Ϭ', 'ϭ', 'Ϯ', 'ϯ', 'ϰ', 'ϱ', 'ϲ', 'ϳ', 'ϴ', 'ϵ', '϶', 'Ϸ', 'ϸ', 'Ϲ', 'Ϻ', 'ϻ', 'ϼ', 'Ͻ', 'Ͼ', 'Ͽ', 'Ⓐ', 'ⓐ', '⒜', 'A', 'a', 'Ạ', 'ạ', 'Ả', 'ả', 'Ḁ', 'ḁ', 'Â', 'Ã', 'Ǎ', 'ǎ', 'Ấ', 'ấ', 'Ầ', 'ầ', 'Ẩ', 'ẩ', 'Ȃ', 'ȃ', 'Ẫ', 'ẫ', 'Ậ', 'ậ', 'À', 'Á', 'Ắ', 'ắ', 'Ằ', 'ằ', 'Ẳ', 'ẳ', 'Ẵ', 'ẵ', 'Ặ', 'ặ', 'Ā', 'ā', 'Ą', 'ą', 'Ǟ', 'Ȁ', 'ȁ', 'Å', 'Ǻ', 'ǻ', 'Ä', 'ä', 'ǟ', 'Ǡ', 'ǡ', 'â', 'á', 'å', 'ã', 'à', 'ẚ', 'Ȧ', 'ȧ', 'Ⱥ', 'Å', 'ⱥ', 'Æ', 'æ', 'Ǽ', 'Ǣ', 'ǣ', 'Ɐ', 'Ꜳ', 'ꜳ', 'Ꜹ', 'Ꜻ', 'Ɑ', 'ꜹ', 'ꜻ', 'ª', '℀', '⅍', '℁', 'Ⓑ', 'ⓑ', '⒝', 'B', 'b', 'Ḃ', 'ḃ', 'Ḅ', 'ḅ', 'Ḇ', 'ḇ', 'Ɓ', 'Ƀ', 'ƀ', 'ƃ', 'Ƃ', 'Ƅ', 'ƅ', 'ℬ', 'Ⓒ', 'ⓒ', '⒞', 'C', 'c', 'Ḉ', 'ḉ', 'Ć', 'ć', 'Ĉ', 'ĉ', 'Ċ', 'ċ', 'Č', 'č', 'Ç', 'ç', 'Ƈ', 'ƈ', 'Ȼ', 'ȼ', 'ℂ', '℃', 'ℭ', 'Ɔ', '℅', '℆', '℄', 'Ꜿ', 'ꜿ', 'Ⓓ', 'ⓓ', '⒟', 'D', 'd', 'Ḋ', 'ḋ', 'Ḍ', 'ḍ', 'Ḏ', 'ḏ', 'Ḑ', 'ḑ', 'Ḓ', 'ḓ', 'Ď', 'ď', 'Ɗ', 'Ƌ', 'ƌ', 'Ɖ', 'Đ', 'đ', 'ȡ', 'ⅅ', 'ⅆ', 'Ǳ', 'ǲ', 'ǳ', 'Ǆ', 'ǅ', 'ǆ', 'ȸ', 'Ⓔ', 'ⓔ', '⒠', 'E', 'e', 'Ḕ', 'ḕ', 'Ḗ', 'ḗ', 'Ḙ', 'ḙ', 'Ḛ', 'ḛ', 'Ḝ', 'ḝ', 'Ẹ', 'ẹ', 'Ẻ', 'ẻ', 'Ế', 'ế', 'Ẽ', 'ẽ', 'Ề', 'ề', 'Ể', 'ể', 'Ễ', 'ễ', 'Ệ', 'ệ', 'Ē', 'ē', 'Ĕ', 'ĕ', 'Ė', 'ė', 'Ę', 'ę', 'Ě', 'ě', 'È', 'è', 'É', 'é', 'Ê', 'ê', 'Ë', 'ë', 'Ȅ', 'ȅ', 'Ȩ', 'ȩ', 'Ȇ', 'ȇ', 'Ǝ', 'ⱸ', 'Ɇ', 'ℇ', 'ℯ', '℮', 'Ɛ', 'ℰ', 'Ə', 'ǝ', 'ⱻ', 'ɇ', 'Ⓕ', 'ⓕ', '⒡', 'F', 'f', 'Ḟ', 'ḟ', 'Ƒ', 'ƒ', 'ꜰ', 'Ⅎ', 'ⅎ', 'ꟻ', 'ℱ', '℻', 'Ⓖ', 'ⓖ', '⒢', 'G', 'g', 'Ɠ', 'Ḡ', 'ḡ', 'Ĝ', 'ĝ', 'Ğ', 'ğ', 'Ġ', 'ġ', 'Ģ', 'ģ', 'Ǥ', 'ǥ', 'Ǧ', 'ǧ', 'Ǵ', 'ℊ', '⅁', 'ǵ', 'Ⓗ', 'ⓗ', '⒣', 'H', 'h', 'Ḣ', 'ḣ', 'Ḥ', 'ḥ', 'Ḧ', 'ḧ', 'Ḩ', 'ḩ', 'Ḫ', 'ḫ', 'ẖ', 'Ĥ', 'ĥ', 'Ȟ', 'ȟ', 'Ħ', 'ħ', 'Ⱨ', 'ⱨ', 'Ꜧ', 'ℍ', 'Ƕ', 'ℏ', 'ℎ', 'ℋ', 'ℌ', 'ꜧ', 'Ⓘ', 'ⓘ', '⒤', 'I', 'i', 'Ḭ', 'ḭ', 'Ḯ', 'ḯ', 'Ĳ', 'ĳ', 'ì', 'í', 'î', 'ï', 'Ì', 'Í', 'Î', 'Ï', 'Ĩ', 'ĩ', 'Ī', 'ī', 'Ĭ', 'ĭ', 'Į', 'į', 'ı', 'Ɨ', 'ƚ', 'Ỻ', 'Ǐ', 'ǐ', 'ⅈ', 'ⅉ', 'ℹ', 'ℑ', 'ℐ', 'Ⓙ', 'ⓙ', '⒥', 'J', 'j', 'Ĵ', 'ĵ', 'ȷ', 'ⱼ', 'Ɉ', 'ɉ', 'ǰ', 'Ⓚ', 'ⓚ', '⒦', 'K', 'k', 'Ḱ', 'ḱ', 'Ḳ', 'ḳ', 'Ḵ', 'ḵ', 'Ķ', 'ķ', 'Ƙ', 'ƙ', 'Ꝁ', 'ꝁ', 'Ꝃ', 'ꝃ', 'Ꝅ', 'ꝅ', 'Ǩ', 'ǩ', 'Ⱪ', 'ⱪ', 'ĸ', 'Ⓛ', 'ⓛ', '⒧', 'L', 'l', 'Ḷ', 'ḷ', 'Ḹ', 'ḹ', 'Ḻ', 'ḻ', 'Ḽ', 'ḽ', 'Ĺ', 'ĺ', 'Ļ', 'ļ', 'Ľ', 'İ', 'ľ', 'Ŀ', 'ŀ', 'Ł', 'ł', 'Ỉ', 'ỉ', 'Ị', 'ị', 'Ƚ', 'Ⱡ', 'Ꝉ', 'ꝉ', 'ⱡ', 'Ɫ', 'ꞁ', 'ℒ', 'Ǉ', 'ǈ', 'ǉ', '⅃', '⅂', 'ℓ', 'ȉ', 'Ȉ', 'Ȋ', 'ȋ', 'Ⓜ', 'ⓜ', '⒨', 'M', 'm', 'Ḿ', 'ḿ', 'Ṁ', 'ṁ', 'Ṃ', 'ṃ', 'ꟿ', 'ꟽ', 'Ɱ', 'Ʃ', 'Ɯ', 'ℳ', 'Ⓝ', 'ⓝ', '⒩', 'N', 'n', 'Ṅ', 'ṅ', 'Ṇ', 'ṇ', 'Ṉ', 'ṉ', 'Ṋ', 'ṋ', 'Ń', 'ń', 'Ņ', 'ņ', 'Ň', 'ň', 'Ǹ', 'ǹ', 'Ŋ', 'Ɲ', 'ñ', 'ŉ', 'Ñ', 'Ƞ', 'ƞ', 'ŋ', 'Ǌ', 'ǋ', 'ǌ', 'ȵ', 'ℕ', '№', 'O', 'o', 'Ṍ', 'ṍ', 'Ṏ', 'ṏ', 'Ṑ', 'ṑ', 'Ṓ', 'ṓ', 'Ȫ', 'ȫ', 'Ȭ', 'ȭ', 'Ȯ', 'ȯ', 'Ȱ', 'ȱ', 'Ǫ', 'ǫ', 'Ǭ', 'ǭ', 'Ọ', 'ọ', 'Ỏ', 'ỏ', 'Ố', 'ố', 'Ồ', 'ồ', 'Ổ', 'ổ', 'Ỗ', 'ỗ', 'Ộ', 'ộ', 'Ớ', 'ớ', 'Ờ', 'ờ', 'Ở', 'ở', 'Ỡ', 'ỡ', 'Ợ', 'ợ', 'Ơ', 'ơ', 'Ō', 'ō', 'Ŏ', 'ŏ', 'Ő', 'ő', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', 'Ǒ', 'Ȍ', 'ȍ', 'Ȏ', 'ȏ', 'Œ', 'œ', 'Ø', 'Ǿ', 'Ꝋ', 'ǽ', 'ǿ', 'ℴ', '⍥', '⍤', 'Ⓞ', 'ⓞ', '⒪', 'ò', 'ó', 'ô', 'õ', 'ö', 'ǒ', 'ø', 'Ꝏ', 'ꝏ', 'Ⓟ', 'ⓟ', '⒫', '℗', 'P', 'p', 'Ṕ', 'ṕ', 'Ṗ', 'ṗ', 'Ƥ', 'ƥ', 'Ᵽ', 'ℙ', 'Ƿ', 'ꟼ', '℘', 'Ⓠ', 'ⓠ', '⒬', 'Q', 'q', 'Ɋ', 'ɋ', 'ℚ', '℺', 'ȹ', 'Ⓡ', 'ⓡ', '⒭', 'R', 'r', 'Ŕ', 'ŕ', 'Ŗ', 'ŗ', 'Ř', 'ř', 'Ṙ', 'ṙ', 'Ṛ', 'ṛ', 'Ṝ', 'ṝ', 'Ṟ', 'ṟ', 'Ȑ', 'ȑ', 'Ȓ', 'ȓ', 'ɍ', 'Ɍ', 'Ʀ', 'Ɽ', '℞', 'Ꝛ', 'ꝛ', 'ℜ', 'ℛ', '℟', 'ℝ', 'Ⓢ', 'ⓢ', '⒮', 'S', 's', 'Ṡ', 'ṡ', 'Ṣ', 'ṣ', 'Ṥ', 'ṥ', 'Ṧ', 'ṧ', 'Ṩ', 'ṩ', 'Ś', 'ś', 'Ŝ', 'ŝ', 'Ş', 'ş', 'Š', 'š', 'Ș', 'ș', 'ȿ', 'ꜱ', 'Ƨ', 'ƨ', 'ẞ', 'ß', 'ẛ', 'ẜ', 'ẝ', '℠', 'Ⓣ', 'ⓣ', '⒯', 'T', 't', 'Ṫ', 'ṫ', 'Ṭ', 'ṭ', 'Ṯ', 'ṯ', 'Ṱ', 'ṱ', 'Ţ', 'ţ', 'Ť', 'ť', 'Ŧ', 'ŧ', 'Ƭ', 'Ʈ', 'ẗ', 'Ț', 'Ⱦ', 'ƫ', 'ƭ', 'ț', 'ⱦ', 'ȶ', '℡', '™', 'Ⓤ', 'ⓤ', '⒰', 'U', 'u', 'Ṳ', 'ṳ', 'Ṵ', 'ṵ', 'Ṷ', 'ṷ', 'Ṹ', 'ṹ', 'Ṻ', 'ṻ', 'Ụ', 'Ủ', 'ủ', 'Ứ', 'Ừ', 'ụ', 'ứ', 'Ử', 'ử', 'ừ', 'ữ', 'Ữ', 'Ự', 'ự', 'Ũ', 'ũ', 'Ū', 'ū', 'Ŭ', 'ŭ', 'Ů', 'ů', 'Ű', 'ű', 'Ǚ', 'ǚ', 'Ǘ', 'ǘ', 'Ǜ', 'ǜ', 'Ų', 'ų', 'Ǔ', 'ǔ', 'Ȕ', 'ȕ', 'Û', 'û', 'Ȗ', 'ȗ', 'Ù', 'ù', 'Ü', 'ü', 'Ư', 'ú', 'Ʉ', 'ư', 'Ʋ', 'Ʊ', 'Ⓥ', 'ⓥ', '⒱', 'V', 'v', 'Ṽ', 'ṽ', 'Ṿ', 'ṿ', 'Ỽ', 'Ʌ', '℣', 'ⱱ', 'ⱴ', 'ⱽ', 'Ⓦ', 'ⓦ', '⒲', 'W', 'w', 'Ẁ', 'ẁ', 'Ẃ', 'ẃ', 'Ẅ', 'ẅ', 'Ẇ', 'ẇ', 'Ẉ', 'ẉ', 'Ŵ', 'ŵ', 'ẘ', 'Ⱳ', 'ⱳ', 'Ⓧ', 'ⓧ', '⒳', 'X', 'x', 'Ẋ', 'ẋ', 'Ẍ', 'ẍ', 'ℵ', '×', 'Ⓨ', 'ⓨ', '⒴', 'y', 'Y', 'Ẏ', 'ẏ', 'Ỿ', 'ỿ', 'ẙ', 'Ỳ', 'ỳ', 'Ỵ', 'ỵ', 'Ỷ', 'ỷ', 'Ỹ', 'ỹ', 'Ŷ', 'ŷ', 'Ƴ', 'ƴ', 'Ÿ', 'ÿ', 'Ý', 'ý', 'Ɏ', 'ɏ', 'Ȳ', 'Ɣ', '⅄', 'ȳ', 'ℽ', 'Ⓩ', 'ⓩ', '⒵', 'Z', 'z', 'Ẑ', 'ẑ', 'Ẓ', 'ẓ', 'Ẕ', 'ẕ', 'Ź', 'ź', 'Ż', 'ż', 'Ž', 'ž', 'Ȥ', 'ȥ', 'Ⱬ', 'ⱬ', 'Ƶ', 'ƶ', 'ɀ', 'ℨ', 'ℤ', '⟀', '⟁', '⟂', '⟃', '⟄', '⟇', '⟈', '⟉', '⟊', '⟐', '⟑', '⟒', '⟓', '⟔', '⟕', '⟖', '⟗', '⟘', '⟙', '⟚', '⟛', '⟜', '⟝', '⟞', '⟟', '⟠', '⟡', '⟢', '⟣', '⟤', '⟥', '⟦', '⟧', '⟨', '⟩', '⟪', '⟫', '⦀', '⦁', '⦂', '⦃', '⦄', '⦅', '⦆', '⦇', '⦈', '⦉', '⦊', '⦋', '⦌', '⦍', '⦎', '⦏', '⦐', '⦑', '⦒', '⦓', '⦔', '⦕', '⦖', '⦗', '⦘', '⦙', '⦚', '⦛', '⦜', '⦝', '⦞', '⦟', '⦠', '⦡', '⦢', '⦣', '⦤', '⦥', '⦦', '⦧', '⦨', '⦩', '⦪', '⦫', '⦬', '⦭', '⦮', '⦯', '⦰', '⦱', '⦲', '⦳', '⦴', '⦵', '⦶', '⦷', '⦸', '⦹', '⦺', '⦻', '⦼', '⦽', '⦾', '⦿', '⧀', '⧁', '⧂', '⧃', '⧄', '⧅', '⧆', '⧇', '⧈', '⧉', '⧊', '⧋', '⧌', '⧍', '⧎', '⧏', '⧐', '⧑', '⧒', '⧓', '⧔', '⧕', '⧖', '⧗', '⧘', '⧙', '⧚', '⧛', '⧜', '⧝', '⧞', '⧟', '⧡', '⧢', '⧣', '⧤', '⧥', '⧦', '⧧', '⧨', '⧩', '⧪', '⧫', '⧬', '⧭', '⧮', '⧯', '⧰', '⧱', '⧲', '⧳', '⧴', '⧵', '⧶', '⧷', '⧸', '⧹', '⧺', '⧻', '⧼', '⧽', '⧾', '⧿', '∀', '∁', '∂', '∃', '∄', '∅', '∆', '∇', '∈', '∉', '∊', '∋', '∌', '∍', '∎', '∏', '∐', '∑', '−', '∓', '∔', '∕', '∖', '∗', '∘', '∙', '√', '∛', '∜', '∝', '∞', '∟', '∠', '∡', '∢', '∣', '∤', '∥', '∦', '∧', '∨', '∩', '∪', '∫', '∬', '∭', '∮', '∯', '∰', '∱', '∲', '∳', '∴', '∵', '∶', '∷', '∸', '∹', '∺', '∻', '∼', '∽', '∾', '∿', '≀', '≁', '≂', '≃', '≄', '≅', '≆', '≇', '≈', '≉', '≊', '≋', '≌', '≍', '≎', '≏', '≐', '≑', '≒', '≓', '≔', '≕', '≖', '≗', '≘', '≙', '≚', '≛', '≜', '≝', '≞', '≟', '≠', '≡', '≢', '≣', '≤', '≥', '≦', '≧', '≨', '≩', '≪', '≫', '≬', '≭', '≮', '≯', '≰', '≱', '≲', '≳', '≴', '≵', '≶', '≷', '≸', '≹', '≺', '≻', '≼', '≽', '≾', '≿', '⊀', '⊁', '⊂', '⊃', '⊄', '⊅', '⊆', '⊇', '⊈', '⊉', '⊊', '⊋', '⊌', '⊍', '⊎', '⊏', '⊐', '⊑', '⊒', '⊓', '⊔', '⊕', '⊖', '⊗', '⊘', '⊙', '⊚', '⊛', '⊜', '⊝', '⊞', '⊟', '⊠', '⊡', '⊢', '⊣', '⊤', '⊥', '⊦', '⊧', '⊨', '⊩', '⊪', '⊫', '⊬', '⊭', '⊮', '⊯', '⊰', '⊱', '⊲', '⊳', '⊴', '⊵', '⊶', '⊷', '⊸', '⊹', '⊺', '⊻', '⊼', '⊽', '⊾', '⊿', '⋀', '⋁', '⋂', '⋃', '⋄', '⋅', '⋆', '⋇', '⋈', '⋉', '⋊', '⋋', '⋌', '⋍', '⋎', '⋏', '⋐', '⋑', '⋒', '⋓', '⋔', '⋕', '⋖', '⋗', '⋘', '⋙', '⋚', '⋛', '⋜', '⋝', '⋞', '⋟', '⋠', '⋡', '⋢', '⋣', '⋤', '⋥', '⋦', '⋧', '⋨', '⋩', '⋪', '⋫', '⋬', '⋭', '⋮', '⋯', '⋰', '⋱', '⋲', '⋳', '⋴', '⋵', '⋶', '⋷', '⋸', '⋹', '⋺', '⋻', '⋼', '⋽', '⋾', '⋿', '✕', '✖', '✚', '◀', '▶', '❝', '❞', '☼', '☺', '♪', '♫', '↺', '↻', '⇖', '⇗', '⇘', '⇙', '⟵', '⟷', '⟶', '➫', '➬', '€', '₤', '＄', '₩', '₪', '◆', '░', '▢', '⊡', '▩', '◎', '◵', '⊗', '❖', 'Ω', 'β', 'Φ', 'Σ', 'Ξ', '⟁', '⦻', '⧉', '⧭', '⧴', '∞', '≌', '⊕', '⋍', '⋰', '⋱', '✖', '⓵', '⓶', '⓷', '⓸', '⓹', '⓺', '⓻', '⓼', '⓽', '⓾', 'ᴕ', '⸨', '⸩', '❪', '❫', '⓵', '⓶', '⓷', '⓸', '⓹', '⓺', '⓻', '⓼', '⓽', '⓾', '⒈', '⒉', '⒊', '⒋', '⒌', '⒍', '⒎', '⒏', '⒐', '⒑', '⒒', '⒓', '⒔', '⒕', '⒖', '⒗', '⒘', '⒙', '⒚', '⒛', '⓪', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩', '➀', '➁', '➂', '➃', '➄', '➅', '➆', '➇', '➈', '➉', '⑪', '⑫', '⑬', '⑭', '⑮', '⑯', '⑰', '⑱', '⑲', '⑳', '⓿', '❶', '❷', '❸', '❹', '❺', '❻', '❼', '❽', '❾', '❿', '➊', '➋', '➌', '➍', '➎', '➏', '➐', '➑', '➒', '➓', '⓫', '⓬', '⓭', '⓮', '⓯', '⓰', '⓱', '⓲', '⓳', '⓴', '⑴', '⑵', '⑶', '⑷', '⑸', '⑹', '⑺', '⑻', '⑼', '⑽', '⑾', '⑿', '⒀', '⒁', '⒂', '⒃', '⒄', '⒅', '⒆', '⒇', 'ᶅ', 'ᶛ', 'ᶜ', 'ᶝ', 'ᶞ', 'ᶟ', 'ᶠ', 'ᶡ', 'ᶢ', 'ᶣ', 'ᶤ', 'ᶥ', 'ᶦ', 'ᶧ', 'ᶨ', 'ᶩ', 'ᶪ', 'ᶫ', 'ᶬ', 'ᶭ', 'ᶮ', 'ᶯ', 'ᶰ', 'ᶱ', 'ᶲ', 'ᶳ', 'ᶴ', 'ᶵ', 'ᶶ', 'ᶷ', 'ᶹ', 'ᶺ', 'ᶻ', 'ᶼ', 'ᶽ', 'ᶾ', 'ᶿ', 'ᴀ', 'ᴁ', 'ᴂ', 'ᴃ', 'ᴄ', 'ᴅ', 'ᴆ', 'ᴇ', 'ᴈ', 'ᴉ', 'ᴊ', 'ᴋ', 'ᴌ', 'ᴍ', 'ᴎ', 'ᴏ', 'ᴐ', 'ᴑ', 'ᴒ', 'ᴓ', 'ᴔ', 'ᴕ', 'ᴖ', 'ᴗ', 'ᴘ', 'ᴙ', 'ᴚ', 'ᴛ', 'ᴜ', 'ᴝ', 'ᴞ', 'ᴟ', 'ᴠ', 'ᴡ', 'ᴢ', 'ᴣ', 'ᴤ', 'ᴥ', 'ᴦ', 'ᴧ', 'ᴨ', 'ᴩ', 'ᴪ', 'ᴫ', 'ᴬ', 'ᴭ', 'ᴮ', 'ᴯ', 'ᴰ', 'ᴱ', 'ᴲ', 'ᴳ', 'ᴴ', 'ᴵ', 'ᴶ', 'ᴷ', 'ᴸ', 'ᴹ', 'ᴺ', 'ᴻ', 'ᴼ', 'ᴽ', 'ᴾ', 'ᴿ', 'ᵀ', 'ᵁ', 'ᵂ', 'ᵃ', 'ᵄ', 'ᵅ', 'ᵆ', 'ᵇ', 'ᵈ', 'ᵉ', 'ᵊ', 'ᵋ', 'ᵌ', 'ᵍ', 'ᵎ', 'ᵏ', 'ᵐ', 'ᵑ', 'ᵒ', 'ᵓ', 'ᵔ', 'ᵕ', 'ᵖ', 'ᵗ', 'ᵘ', 'ᵙ', 'ᵚ', 'ᵛ', 'ᵜ', 'ᵝ', 'ᵞ', 'ᵟ', 'ᵠ', 'ᵡ', 'ᵢ', 'ᵣ', 'ᵤ', 'ᵥ', 'ᵦ', 'ᵧ', 'ᵨ', 'ᵩ', 'ᵪ', 'ᵫ', 'ᵬ', 'ᵭ', 'ᵮ', 'ᵱ', 'ᵲ', 'ᵳ', 'ᵵ', 'ᵷ', 'ᵸ', 'ᵺ', 'ᵻ', '«', '»', '‹', '›', '<', '>', '@', '‧', '¨', '․', '꞉', ':', '⁚', '⁝', '⁞', '‥', '…', '⁖', '⸪', '⸬', '⸫', '⸭', '⁛', '⁘', '⁙', '⁏', ';', '⁃', '‐', '‑', '‒', '-', '–', '—', '―', '_', '⁓', '⸛', '⸞', '⸟', 'ⸯ', '¬', '/', '\\', '⁄', '\\', '⁄', '|', '⎜', '¦', '‖', '‗', '†', '‡', '·', '•', '⸰', '°', '‣', '⁒', '%', '‰', '‱', '&', '⅋', '§', '÷', '+', '±', '=', '꞊', '′', '″', '‴', '⁗', '‵', '‶', '‷', '‸', '*', '⁑', '⁎', '⁕', '※', '⁜', '⁂', '!', '‼', '¡', '?', '¿', '⸮', '⁇', '⁉', '⁈', '‽', '⸘', '¼', '½', '¾', '²', '³', '©', '®', '™', '℠', '℻', '℅', '℁', '⅍', '℄', '¶', '⁋', '⁌', '⁍', '⸖', '⸗', '⸚', '⸓', '(', ')', '[', ']', '{', '}', '⸨', '⸩', '❨', '❩', '❪', '❫', '⸦', '⸧', '❬', '❭', '❮', '❯', '❰', '❱', '❴', '❵', '❲', '❳', '⦗', '⦘', '⁅', '⁆', '〈', '〉', '⏜', '⏝', '⏞', '⏟', '⸡', '⸠', '⸢', '⸣', '⸤', '⸥', '⎡', '⎤', '⎣', '⎦', '⎨', '⎬', '⌠', '⌡', '⎛', '⎠', '⎝', '⎞', '⁀', '⁔', '‿', '⁐', '‾', '⎟', '⎢', '⎥', '⎪', 'ꞁ', '⎮', '⎧', '⎫', '⎩', '⎭', '⎰', '⎱', '✈', '☀', '☼', '☁', '☂', '❄', '❅', '❆', '☃', '☉', '☄', '★', '☆', '☽', '☾', '☇', '☈', '⌂', '⌁', '⏧', '✆', '☎', '☏', '☑', '✓', '✔', '⎷', '⍻', '✖', '✗', '✘', '☒', '✕', '☓', '☚', '☛', '☜', '☞', '☟', '☹', '☺', '☻', '☯', '⚘', '☮', '✝', '⚰', '⚱', '⚠', '☠', '☢', '⚔', '⎈', '⚒', '⚑', '⚐', '☡', '❂', '⚕', '⚖', '⚗', '✇', '☣', '⚙', '☤', '⚚', '⚛', '⚜', '☥', '☦', '☧', '☨', '☩', '†', '☪', '☫', '☬', '☭', '✁', '✂', '✃', '✄', '✎', '✏', '✐']

print(fore.VIOLET+"   ,-. ,------. ,-.    ")
print("  /  |/  .--.  '|  \   ")
print(" /  .'|  |  |  |'.  \  ")
print("/  /  `--'__.  |  \  \ ")
print("\  \     |   .'   /  / ")
print(" \  '.   |___|  .'  /  ")
print("  \  |   .---.  |  /   ")
print("   `-'   `---'  `-'    "+fore.WHITE)
time.sleep(1)
print("\narchCrypter 1.0.0      © Enrico Fracasso 2022")
time.sleep(1)
while True:
  a = random.choice(chars)
  b = random.choice(chars)
  c = random.choice(chars)
  d = random.choice(chars)
  e = random.choice(chars)
  f = random.choice(chars)
  g = random.choice(chars)
  h = random.choice(chars)
  i = random.choice(chars)
  j = random.choice(chars)
  k = random.choice(chars)
  l = random.choice(chars)
  m = random.choice(chars)
  n = random.choice(chars)
  o = random.choice(chars)
  p = random.choice(chars)
  q = random.choice(chars)
  r = random.choice(chars)
  s = random.choice(chars)
  t = random.choice(chars)
  u = random.choice(chars)
  v = random.choice(chars)
  w = random.choice(chars)
  x = random.choice(chars)
  y = random.choice(chars)
  z = random.choice(chars)
  uno = random.choice(chars)
  due = random.choice(chars)
  tre = random.choice(chars)
  quattro = random.choice(chars)
  cinque = random.choice(chars)
  sei = random.choice(chars)
  sette = random.choice(chars)
  otto = random.choice(chars)
  nove = random.choice(chars)
  zero = random.choice(chars)

  letters_to_symbols = {
    'A': a,
    'B': b,
    'C': c,
    'D': d,
    'E': e,
    'F': f,
    'G': g,
    'H': h,
    'I': i,
    'J': j,
    'K': k,
    'L': l,
    'M': m,
    'N': n,
    'O': o,
    'P': p,
    'Q': q,
    'R': r,
    'S': s,
    'T': t,
    'U': u,
    'V': v,
    'W': w,
    'X': x,
    'Y': y,
    'Z': z,
    '1': uno,
    '2': due,
    '3': tre,
    '4': quattro,
    '5': cinque,
    '6': sei,
    '7': sette,
    '8': otto,
    '9': nove,
    '0': zero,
  }

  isEnt = input('\n\nType here something you want to encrypt:\n\n')
  print(fore.BLUE+"\nEncrypting..."+fore.WHITE)
  time.sleep(2)
  print(fore.BLUE+"\nEncrypted!\n"+fore.WHITE)

  for letter, symbol in letters_to_symbols.items():
    isEnt = isEnt.replace(letter, symbol)
    isEnt = isEnt.replace(letter.lower(), symbol)
  
  print(isEnt)
  time.sleep(0.5)
  print("\nDecryption key:\n"+fore.VIOLET + a + b + c + d + e + f + g + h + i + j +
      k + l + m + n + o + p + q + r + s + t + u + v + w + x + y + z + uno +
      due + tre + quattro + cinque + sei + sette + otto + nove + zero+fore.WHITE)

  symbols_to_letters = {
    a: 'a',
    b: 'b',
    c: 'c',
    d: 'd',
    e: 'e',
    f: 'f',
    g: 'g',
    h: 'h',
    i: 'i',
    j: 'j',
    k: 'k',
    l: 'l',
    m: 'm',
    n: 'n',
    o: 'o',
    p: 'p',
    q: 'q',
    r: 'r',
    s: 's',
    t: 't',
    u: 'u',
    v: 'v',
    w: 'w',
    x: 'x',
    y: 'y',
    z: 'z',
    uno: '1',
    due: '2',
    tre: '3',
    quattro: '4',
    cinque: '5',
    sei: '6',
    sette: '7',
    otto: '8',
    nove: '9',
    zero: '0',
  }

  isOut = ""
  isOut = isEnt

  print(fore.BLUE+"\nDecripting using the decryption key...\n"+fore.WHITE)
  for letter, symbol in symbols_to_letters.items():
    isOut = isOut.replace(letter, symbol)
    isOut = isOut.replace(letter.lower(), symbol)
  time.sleep(2)
  print(isOut)
  time.sleep(0.5)
  chioce=input("\n\nType 'back' to quit archCrypter, or just press ENTER without typing to crypt something else\n")
  if chioce =="back":
    replit.clear()
    print("Returning to apllications list...")
    time.sleep(2)
    replit.clear()
    exec(open("apps.py").read())
    break
  else:
    replit.clear()
    print(fore.VIOLET+"   ,-. ,------. ,-.    ")
    print("  /  |/  .--.  '|  \   ")
    print(" /  .'|  |  |  |'.  \  ")
    print("/  /  `--'__.  |  \  \ ")
    print("\  \     |   .'   /  / ")
    print(" \  '.   |___|  .'  /  ")
    print("  \  |   .---.  |  /   ")
    print("   `-'   `---'  `-'    "+fore.WHITE)
    print("\narchCrypter 1.0.0      © Enrico Fracasso 2022")
    True