# -*- coding: utf-8 -*-
#

SAMPLE_SCC_CREATED_DFXP_WITH_WRONGLY_CLOSING_SPANS = """\
Scenarist_SCC V1.0

00:01:28;09 9420 942f 94ae 9420 9452 97a2 e3e3 e3e3 e3e3 9470 9723 e3a1 e3a1

00:01:31;10 9420 942f 94ae

00:01:31;18 9420 9454 6262 6262 9458 97a1 91ae e3e3 e3e3 9470 97a1 6262 6161

00:01:35;18 9420 942f 94ae

00:01:40;25 942c

00:01:51;18 9420 9452 97a1 6161 94da 97a2 91ae 6262 9470 97a1 e3e3

00:01:55;22 9420 942f 6162 e364 94f4 9723 6162 e364

00:01:59;14 9420 942f 94ae 9420 94f4 6464 6464
"""

SCC_THAT_GENERATES_WEBVTT_WITH_PROPER_NEWLINES = """\
Scenarist_SCC V1.0

00:21:29;23    9420 9452 6161 94f4 97a2 6262 942c 942f
"""

SAMPLE_SCC_PRODUCES_CAPTIONS_WITH_START_AND_END_TIME_THE_SAME = """\
Scenarist_SCC V1.0

00:01:31;18 9420 9454 6162 9758 97a1 91ae 6261 9170 97a1 e362

00:01:35;18 9420 942f 94ae

00:01:40;25 942c
"""

SAMPLE_SCC_POP_ON = """Scenarist_SCC V1.0

00:00:09:05 94ae 94ae 9420 9420 9470 9470 a820 e3ec efe3 6b20 f4e9 e36b e96e 6720 2980 942c 942c 942f 942f

00:00:12:08 942c 942c

00:00:13:18 94ae 94ae 9420 9420 1370 1370 cdc1 ceba 94d0 94d0 5768 e56e 20f7 e520 f468 e96e 6b80 9470 9470 efe6 20a2 4520 e5f1 7561 ec73 206d 20e3 ad73 f175 61f2 e564 a22c 942c 942c 942f 942f

00:00:16:03 94ae 94ae 9420 9420 9470 9470 f7e5 2068 6176 e520 f468 e973 2076 e973 e9ef 6e20 efe6 2045 e96e 73f4 e5e9 6e80 942c 942c 942f 942f

00:00:17:20 94ae 94ae 9420 9420 94d0 94d0 6173 2061 6e20 efec 642c 20f7 f2e9 6e6b ec79 206d 616e 9470 9470 f7e9 f468 20f7 68e9 f4e5 2068 61e9 f2ae 942c 942c 942f 942f

00:00:19:13 94ae 94ae 9420 9420 1370 1370 cdc1 ce20 32ba 94d0 94d0 4520 e5f1 7561 ec73 206d 20e3 ad73 f175 61f2 e564 20e9 7380 9470 9470 6eef f420 6162 ef75 f420 616e 20ef ec64 2045 e96e 73f4 e5e9 6eae 942c 942c 942f 942f

00:00:25:16 94ae 94ae 9420 9420 1370 1370 cdc1 ce20 32ba 94d0 94d0 49f4 a773 2061 ecec 2061 62ef 75f4 2061 6e20 e5f4 e5f2 6e61 ec80 9470 9470 45e9 6e73 f4e5 e96e ae80 942c 942c 942f 942f

00:00:31:15 94ae 94ae 9420 9420 9470 9470 bc4c c1d5 c7c8 49ce c720 2620 57c8 4f4f d0d3 a13e 942c 942c 942f 942f

00:00:36:04 942c 942c

"""

# 6 captions
#   2 Pop-On captions.
#       The first has 3 random positions, and thus 3 captions
#       The second should be interpreted as 1 caption with 2 line breaks
#   2 Roll-Up captions - same comment
#   2 Paint-on captions - same comment
#       - the TAB OVER commands are not interpreted (97A1, 97A2, 9723)
SAMPLE_SCC_MULTIPLE_POSITIONING = """Scenarist_SCC V1.0

00:00:00:16 94ae 94ae 9420 9420 1370 1370 6162 6162 91d6 91d6 e364 e364 927c 927c e5e6 e5e6 942c 942c 942f 942f

00:00:02:16 94ae 94ae 9420 9420 16f2 16f2 6768 6768 9752 9752 e9ea e9ea 97f2 97f2 6bec 6bec 942c 942c 942f 942f

00:00:09:21    9425 9425 94ad 94ad 94f2 94f2 6d6e 6d6e 97d6 97d6 ef70 ef70 92dc 92dc f1f2 f1f2

00:00:11:21 9425 9425 94ad 94ad 15f2 15f2 73f4 73f4 1652 1652 7576 7576 16f2 f7f8 f7f8

00:00:20;02    9429 9429 9452 9452 97A2 97A2 797A 797A 917c 917c B031 B031 16d6 16d6 32B3 32B3

00:00:22;02    9429 9429 1352 1352 97A2 97A2 34B5 34B5 13f2 13f2 B637 B637 9452 9452 38B9 38B9

00:00:36:04 942c 942c

"""

# UNUSED SAMPLE
SAMPLE_SCC_WITH_ITALICS_BKUP = """\
Scenarist_SCC V1.0

00:00:00:01 9420 10d0 97a2 91ae 6162 6162 6162 6162 942c 8080 8080 942f
"""

SAMPLE_SCC_WITH_ITALICS = """\

00:00:00:01 9420 10d0 97a2 91ae 6162 6162 6162 6162 942c 8080 8080 942f
"""


SAMPLE_SCC_EMPTY = """Scenarist_SCC V1.0
"""

SAMPLE_SCC_ROLL_UP_RU2 = """\
Scenarist_SCC V1.0
00:00:00;22    9425 9425 94ad 94ad 9470 9470 3e3e 3e20 c849 ae

00:00:02;23    9425 9425 94ad 94ad 9470 9470 49a7 cd20 cb45 d649 ce20 43d5 cece 49ce c720 c1ce c420 c154

00:00:04;17    9425 9425 94ad 94ad 9470 9470 49ce d645 d354 4f52 a7d3 20c2 c1ce cb20 5745 20c2 454c 4945 d645 2049 ce

00:00:06;04    9425 9425 94ad 94ad 9470 9470 c845 4cd0 49ce c720 54c8 4520 4c4f 43c1 4c20 ce45 49c7 c8c2 4f52 c84f 4fc4 d3

00:00:09;21    9425 9425 94ad 94ad 9470 9470 c1ce c420 49cd d052 4fd6 49ce c720 54c8 4520 4c49 d645 d320 4f46 20c1 4c4c

00:00:11;07    9425 9425 94ad 94ad 9470 9470 5745 20d3 4552 d645 ae

00:00:12;07    9425 9425 94ad 94ad 9470 9470 91b0 9131 9132 9132

00:00:13;07    9425 9425 94ad 94ad 9470 9470 c1c2 c3c4 c580 91bf

00:00:14;07    9425 9425 94ad 94ad 9470 9470 9220 9220 92a1 92a2 92a7

00:00:17;01    9426 9426 94ad 94ad 9470 9470 57c8 4552 4520 d94f d5a7 5245 20d3 54c1 cec4 49ce c720 ce4f 572c

00:00:18;19    9426 9426 94ad 94ad 9470 9470 4c4f 4fcb 49ce c720 4fd5 5420 54c8 4552 452c 2054 c8c1 54a7 d320 c14c 4c

00:00:20;06    9426 9426 94ad 94ad 9470 9470 54c8 4520 4352 4f57 c4ae

00:00:21;24    9426 9426 94ad 94ad 9470 9470 3e3e 2049 5420 57c1 d320 c74f 4fc4 2054 4f20 c245 2049 ce20 54c8 45

00:00:34;27    94a7 94ad 9470 c16e 6420 f2e5 73f4 eff2 e520 49ef f761 a773 20ec 616e 642c 20f7 61f4 e5f2

00:00:36;12    94a7 94ad 9470 c16e 6420 f7e9 ec64 ece9 e6e5 ae80

00:00:44;08    94a7 94ad 9470 3e3e 20c2 e96b e520 49ef f761 2c20 79ef 75f2 2073 ef75 f2e3 e520 e6ef f280
"""


SAMPLE_SCC_PRODUCES_BAD_LAST_END_TIME = """\
Scenarist_SCC V1.0

00:23:28;01    9420 94ae 9154 5245 91f4 c1c2 942c

00:24:29;21    942f

00:53:28;01    9420 94ae 9154 4552 91f4 aeae 942c

00:54:29;21    942f
"""

SAMPLE_NO_POSITIONING_AT_ALL_SCC = """\
Scenarist_SCC V1.0

00:23:28;01    9420 94ae 5245 c1c2 942c

00:24:29;21    942f

00:53:28;01    9420 94ae 4552 aeae 942c

00:54:29;21    942f
"""

# UNUSED SAMPLE
SAMPLE_SCC_NOT_EXPLICITLY_SWITCHING_ITALICS_OFF = """\
Scenarist_SCC V1.0

00:01:28;09    9420 942f 94ae 9420 9452 97a2 b031 6161 9470 9723 b031 6262

00:01:31;10    9420 942f 94ae

00:01:31;18    9420 9454 b032 e3e3 9458 97a1 91ae b032 6464 9470 97a1 b032 e5e5

00:01:35;18    9420 942f 94ae

00:01:40;25    942c

00:01:51;18    9420 9452 97a1 b0b3 6161 94da 97a2 91ae b0b3 6262 9470 97a1 b0b3 e3e3

00:01:55;22    9420 942f b034 6161 94f4 9723 b034 6262

00:01:59;14    9420 942f 94ae 9420 94f4 b034 3180 e3e3

00:02:02;01    9420 942f 94ae 9420 94d0 b0b5 6161 94f2 97a2 b0b5 6262

00:02:04;05    9420 942f 94ae

00:09:53;06    942c 9420 13f4 9723 b0b6 e3e3 9454 97a2 b0b6 6464 9470 97a2 b0b6 e5e5

00:09:56;09    9420 942f 94ae 9420 94f2 b037 6161

00:09:58;18    9420 942f 94ae 9420 9454 b038 6262 9454 97a2 91ae b038 e3e3 94f2 97a1 94f2 97a1 91ae b038 6162 6464

00:09:59;28    9420 942f 94ae 9420 9452 97a2 e5e5 94f4 b0b9 6161

00:10:02;22    9420 942f 94ae 9420 9452 97a1 31b0 e5e5 9470 97a2 31b0 6262

00:10:04;10    9420 942f 94ae

00:52:03;02    9420 9470 97a2 3131 e3e3

00:52:18;20    9420 91d0 9723 3132 6464 9158 97a1 91ae 3132 e5e5 91da 97a2 9120 3132 6161 91f2 9723 3132 6262

00:52:22;22    9420 942c 942f 9420 9152 97a2 31b3 e3e3

00:52:25;04    9420 942c 942f 9420 91d0 97a2 3134 6464 91f2 e5e5

00:52:26;28    9420 942c 942f

00:52:27;18    9420 9152 9152 9152 91ae 31b5 6161 9154 97a1 9120 31b5 6262 9170 9723 31b5 e3e3

00:52:31;22    9420 942c 942f

00:52:34;14    942c

00:53:03;15    9420 94f4 97a1 94f4 97a1 91ae 31b6 6464
"""

SAMPLE_SCC_NO_EXPLICIT_END_TO_LAST_CAPTION = """\
Scenarist_SCC V1.0

00:00:00;00    73e9 e329 942f

00:00:06;01    942c

00:24:55;14    9420 94ae 9470 97a2 a875 7062 e561 f420 f2ef e36b 206d 7573 e9e3 2980 942f
"""

SAMPLE_SCC_FLASHING_CAPTIONS = """\
Scenarist_SCC V1.0

00:00:00;20 9420 9420 942c 942c 942f 942f 9420 9420 9152 9152 4fd5 5220 cec1 5449 4fce c14c 20d0 c152 cbd3 91f2 91f2 c245 4c4f cec7 2054 4f20 c14c 4c20 4f46 20d5 d3ae

00:00:02;02 9420 9420 942c 942c 942f 942f 9420 9420 91d0 91d0 54c8 45d9 20c1 5245 20d0 4cc1 4345 d320 4f46 20c4 49d3 434f d645 52d9 2c80 9170 9170 54c8 45d9 20c1 5245 20d0 4cc1 4345 d320 4f46 2049 ced3 d049 52c1 5449 4fce 2c80

00:00:04;29 9420 9420 942c 942c 942f 942f

00:00:06;08 9420 9420 9154 9154 54c8 45d9 20c1 5245 91f2 91f2 c1cd 4552 4943 c1a7 d320 c245 d354 2049 c445 c1ae

00:00:09;24 9420 9420 942c 942c 942f 942f

00:00:10;06 9420 9420 9152 9152 cdc1 4a4f 5220 46d5 cec4 49ce c720 d052 4fd6 49c4 45c4 20c2 d980

00:00:13;19 9420 9420 942c 942c 942f 942f 9420 9420 9154 9154 54c8 4520 45d6 454c d9ce 9170 9170 c1ce c420 57c1 4c54 4552 20c8 c1c1 d32c 204a 52ae 2046 d5ce c4ae

00:00:15;11 9420 9420 942c 942c 942f 942f

00:00:16;08 9420 9420 9152 9152 c1c4 c449 5449 4fce c14c 2046 d5ce c449 cec7 91f2 91f2 57c1 d320 d052 4fd6 49c4 45c4 20c2 d9ba

00:00:19;19 9420 94ae 9152 9723 c1c4 c449 5449 4fce c14c 2046 d5ce c449 cec7 91f4 57c1 d320 d052 4fd6 49c4 45c4 20c2 d9ba 942c

00:00:20;13 942f

00:00:21;19 9420 94ae 9152 9723 54c8 4520 d0c1 52cb 2046 4fd5 cec4 c154 494f ce80 942c

00:00:22;07 942f

00:00:22;14 9420 94ae 9152 97a2 49ce 20d3 d5d0 d04f 5254 204f 4620 c120 434c 45c1 ce80 91f2 c1ce c420 c845 c14c 54c8 d920 45ce d649 524f cecd 45ce 543b 942c

00:00:23;15 942f

00:00:25;09 9420 94ae 9152 97a1 54c8 4520 c152 54c8 d552 20d6 49ce 49ce c720 c4c1 d649 d380 91f4 97a2 464f d5ce c4c1 5449 4fce d32c 942c

00:00:26;06 942f

00:00:27;15 9420 94ae 91d0 9723 c445 c449 43c1 5445 c420 544f 20d3 5452 45ce c754 c845 ce49 cec7 91f4 c1cd 4552 4943 c1a7 d320 46d5 54d5 5245 942c

00:00:28;14 942f
"""


SAMPLE_SCC_EOC_FIRST_COMMAND = """\
Scenarist_SCC V1.0

00:00:00;84    942f

00:00:02;00    73e9 e329 942f

00:00:06;01    942c

00:24:55;14    9420 94ae 9470 97a2 a875 7062 e561 f420 f2ef e36b 206d 7573 e9e3 2980 942f

00:25:00;00    942c
"""


SAMPLE_SCC_SPACE_PRIOR_TO_ITALIC_COMMAND = """\
Scenarist_SCC V1.0

00:00:00:00     942c

00:00:00:18     9420 94f2 5b43 6875 e36b 5d20 91ae c8e5 792c 2049 a76d 2043 6875 e36b ae80 942c 942f

00:00:01:06     942c
"""


SAMPLE_SCC_ITALICS_MIDROW_CODE = """\
Scenarist_SCC V1.0

00:00:08:07     942c

00:00:20:02     9420 94ae 9454 91b9 e6f2 ef6d 91ae da61 ecec 20c7 efef 6480 94f2 91b9 91b9 f7e9 f468 20c1 ece5 f8e9 7320 c7ae 20da 61ec ecae 942c 8080 8080 942f

00:00:21:23     942c
"""
