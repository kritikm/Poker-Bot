#File Contains the likelihood probabilites i.e P(x/w(i))

prior_probabilities = [1.50e-06,1.38e-05,0.00024,0.00144,0.00198,0.00355,0.02353,0.10372,0.58823,1]



    #   Royal      Straight   4kind    Full     Flush     Straight  3kind    2pair    1pair     high card
    #   Flush     Flush               House
likelihood = {

#Clubs
'C2':	[0.00000,     0.00000,    0.01494,    0.01651,    0.04171,    0.00185,    0.01376,    0.00757,    0.01488,    0.01215],

'C3':	[0.00000,     0.00000,    0.02955,    0.01680,    0.05734,    0.00567,    0.01659,    0.00936,    0.01627,    0.01194],

'C4':	[0.00000,     0.05351,    0.03796,    0.01503,    0.04356,    0.00873,    0.01160,    0.01053,    0.01494,    0.01245],

'C5':	[0.00000,     0.05351,    0.01969,    0.01735,    0.04714,    0.00741,    0.01383,    0.01019,    0.01499,    0.01224],

'C6':	[0.00000,     0.05351,    0.01997,    0.01393,    0.04025,    0.01400,    0.01282,    0.01059,    0.01526,    0.01286],

'C7':	[0.00000,     0.00000,    0.03510,    0.01175,    0.03284,    0.01022,    0.01328,    0.01013,    0.01551,    0.01281],

'C8':	[0.00000,     0.06933,    0.01961,    0.00893,    0.03526,    0.00930,    0.01143,    0.01038,    0.01642,    0.01236],

'C9':	[0.00000,     0.14649,    0.01071,    0.02052,    0.03039,    0.01309,    0.01273,    0.01189,    0.01592,    0.01275],

'C10':	[0.00000,     0.14649,    0.02588,    0.01088,    0.03532,    0.01148,    0.01436,    0.01004,    0.01612,    0.01238],

'CJ':	[0.00000,	  0.07716,    0.03036,    0.01577,    0.02071,    0.00739,    0.01391,    0.01021,    0.01584,    0.01226],

'CQ':	[0.00000	,0.00000	,0.02287	,0.01760	,0.01725,	0.00605	,0.01074	,0.01029	,0.01657,	0.01210],

'CK':    [0.00000	,0.00000	,0.00856	,0.01668	,0.01605	,0.00327	,0.01099	,0.00884	,0.01642,	0.01256],

'CA':	[0.00000	,0.00000	,0.00902,	0.00808	,0.01525	,0.00094	,0.01385,	0.00741	,0.01668,	0.01270],

#Diamonds
'D2':	[0.00000,	0.00000	,0.01569	,0.01311,	0.00000,	0.00250,	0.01421,	0.00697,	0.01554,	0.01286],

'D3':	[0.00000	,0.00000	,0.01861	,0.01408	,0.00016,	0.00249,	0.01421	,0.00771	,0.01438	,0.01237],

'D4':	[0.00000,	0.00000	,0.02074,	0.01551	,0.00089,	0.00644,	0.01037,	0.00969,	0.01366,	0.01315],

'D5':	[0.00000	,0.00000	,0.01170	,0.01870	,0.00175	,0.00722	,0.01339	,0.01045	,0.01482	,0.01240],

'D6':	[0.00000,	0.00000,	0.01277,	0.01286,	0.00182	,0.00963	,0.01099,	0.00975,	0.01454,	0.01318],

'D7':	[0.00000	,0.00000	,0.01396	,0.01191,	0.00019,	0.00898,	0.01228,	0.01062	,0.01560,	0.01250],

'D8':	[0.00000,	0.00000,	0.03266	,0.01182,	0.00384	,0.01325	,0.01149	,0.01141	,0.01519,	0.01228],

'D9':	[0.00000	,0.00000	,0.02251,	0.01414	,0.00634	,0.00907	,0.01372	,0.01083,	0.01605,	0.01243],

'D10':	[0.00000,	0.00000,	0.01030,	0.01480,	0.00922,	0.01100	,0.01330	,0.00874,	0.01607,	0.01305],

'DJ':	[0.00000	,0.06933	,0.01485	,0.01301,	0.00931,	0.00679	,0.01210	,0.00892	,0.01624	,0.01274],

'DQ':	[0.00000,	0.06933,	0.01420,	0.02061,	0.00825,	0.00638,	0.01187	,0.00984	,0.01573,	0.01271],

'DK':	[0.00000,	0.00000,	0.01544	,0.01428	,0.00814,	0.00378,	0.01015	,0.00807	,0.01603	,0.01272],

'DA':	[0.00000,	0.00000,	0.01967	,0.01442	,0.00871	,0.00247	,0.01386,	0.00695,	0.01638,	0.01215],

#Hearts
'H2':	[0.00000, 0.00000,	0.02362,	0.02007	,0.00000,	0.00319,	0.01400	,0.00719	,0.01461	,0.01163],

'H3':	[0.00000	,0.00000,	0.01647,	0.01827,	0.00000	,0.00428	,0.01220,	0.00936,	0.01459,	0.01285],

'H4':	[0.00000	,0.00000	,0.01427	,0.01515	,0.00000	,0.00424	,0.01153	,0.00914	,0.01424,	0.01246],

'H5':	[0.00000,	0.00000,	0.02715,	0.01903	,0.00076	,0.01007	,0.01590,	0.01091,	0.01725,	0.01140],

'H6':	[0.00000,	0.00000	,0.01605	,0.00879,	0.00135,	0.01066,	0.01033	,0.01083	,0.01434	,0.01343],

'H7':	[0.00000	,0.05351	,0.01639	,0.01117	,0.00186,	0.01245	,0.01192,	0.01083	,0.01652,	0.01288],

'H8':	[0.00000	,0.05351	,0.01720	,0.01055	,0.00261	,0.00946	,0.01150	,0.01135	,0.01651	,0.01223],

'H9':	[0.00000	,0.00000	,0.01241	,0.01392,	0.00444	,0.01011	,0.01436	,0.00985	,0.01656	,0.01288],

'H10':	[0.00000	,0.00000	,0.00934	,0.01367	,0.00568,	0.01165,	0.01077,	0.01043	,0.01575	,0.01258],

'HJ':	[0.00000	,0.00000	,0.01801	,0.01702	,0.00802	,0.00762,	0.01327,	0.01137,	0.01553	,0.01210],

'HQ':	[0.00000	,0.07716,	0.01378,	0.02242,	0.00969,	0.00661,	0.01062,	0.00969,	0.01596	,0.01264],

'HK':	[0.00000	,0.07716,	0.00873,	0.01451,	0.01223,	0.00428,	0.00935,	0.00729,	0.01539,	0.01305],

'HA':	[0.00000	,0.00000,	0.01757	,0.01775	,0.00845,	0.00187,	0.01419	,0.00705	,0.01615,	0.01232],

#Spades
'S2':	[0.00000	,0.00000,	0.03369	,0.01567	,0.00000	,0.00164	,0.01233,	0.00668	,0.01368,	0.01237],

'S3':	[0.00000	,0.00000	,0.02090	,0.01297	,0.00000	,0.00514,	0.01149	,0.00839	,0.01403	,0.01268],

'S4':	[0.00000	,0.00000,	0.02182,	0.01594	,0.00000,	0.00767,	0.01156, 0.00936,	0.01469	,0.01244],

'S5':	[0.00000	,0.00000	,0.02130	,0.01348,	0.00000,	0.00855,	0.01302,	0.01047,	0.01528,	0.01251],

'S6':	[0.00000	,0.00000	,0.01260,	0.01267,	0.00254,	0.01050,	0.01339,	0.00900,	0.01332	,0.01247],

'S7':	[0.00000	,0.00000,	0.02488	,0.01932	,0.00139,	0.01262,	0.01266,	0.01032,	0.01420,	0.01206],

'S8':	[0.00000	,0.00000	,0.02380	,0.01356	,0.00348	,0.01251,	0.01265,	0.01018,	0.01475	,0.01298],

'S9':	[0.00000	,0.00000,	0.01470,	0.01358,	0.00182,	0.01046,	0.01018,	0.01100,	0.01538	,0.01257],

'S10':	[0.00000	,0.00000,	0.01259	,0.01097	,0.00686	,0.00999	,0.00882	,0.01050	,0.01566	,0.01260],

'SJ':	[0.00000	,0.00000	,0.01198,	0.01377,	0.01169,	0.01077,	0.01069,	0.01013,	0.01669	,0.01219],

'SQ':	[0.00000	,0.00000	,0.01416	,0.01536	,0.00972	,0.00487	,0.01151	,0.00936	,0.01705	,0.01174],

'SK': [0.00000	,0.00000,	0.01967,	0.01515	,0.01210,	0.00392,	0.01210,	0.00866,	0.01616	,0.01267],

'SA':	[0.00000	,0.00000	,0.01513	,0.01329	,0.00742,	0.00225	,0.01105	,0.00658	,0.01703,	0.01207]
}
