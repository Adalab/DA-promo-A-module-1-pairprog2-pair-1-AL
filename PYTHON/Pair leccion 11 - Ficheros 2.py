import os
import xml.etree.ElementTree as ET

#Funcion 1
#Si el fichero no existe, debe crearlo, insertar contenido y mostrar su contenido.
#Si el fichero existe pregunta al usuario si quiere sobreescribirlo. 
#En caso de Si, sobreescribe el fichero, insertad contenido y leedlo. En caso de No, no hace nada.

def lectura_txt(nombre, mode, encoding, contenido):
    ubicacion = './' + nombre
    
    if nombre in os.listdir():
       print('El archivo ya existe. ¿Quieres sobreescribirlo?')
       respuesta = input('S/N: ')
       if respuesta == 'S':
            file = open(ubicacion, "w")
            file.write(contenido)
            file.close()
    else:
       print('El fichero no existe, se va a crear con el nombre', nombre)
       file = open(ubicacion, "w")
       file.write(contenido)
       print(file.read())
       file.close()

lectura_txt('email.txt', 'rt', encoding = 'utf-8', contenido = """

      Thu Oct 31 08:11:39 2002
        Return-Path: <bensul2004nng@spinfinder.com>
        X-Sieve: cmu-sieve 2.0
        Return-Path: <bensul2004nng@spinfinder.com>
        Message-Id: <200210311310.g9VDANt24674@bloodwork.mr.itd.UM>
        From: "Mr. Ben Suleman" <bensul2004nng@spinfinder.com>
        Date: Thu, 31 Oct 2002 05:10:00
        To: R@M
        Subject: URGENT ASSISTANCE /RELATIONSHIP (P)
        MIME-Version: 1.0
        Content-Type: text/plain;charset="iso-8859-1"
        Content-Transfer-Encoding: 7bit
        Status: O

        Dear Friend,

        I am Mr. Ben Suleman a custom officer and work as Assistant controller of the Customs and Excise department Of the Federal Ministry of Internal Affairs stationed at the Murtala Mohammed International Airport, Ikeja, Lagos-Nigeria.

        After the sudden death of the former Head of state of Nigeria General Sanni Abacha on June 8th 1998 his aides and immediate members of his family were arrested while trying to escape from Nigeria in a Chartered jet to Saudi Arabia with 6 trunk boxes Marked "Diplomatic Baggage". Acting on a tip-off as they attempted to board the Air Craft,my officials carried out a thorough search on the air craft and discovered that the 6 trunk boxes contained foreign currencies amounting to US$197,570,000.00(One Hundred and  Ninety-Seven Million Five Hundred Seventy Thousand United States Dollars).

        I declared only (5) five boxes to the government and withheld one (1) in my custody containing the sum of (US$30,000,000.00) Thirty Million United States Dollars Only, which has been disguised to prevent their being discovered during transportation process.Due to several media reports on the late head of state about all the money him and his co-government officials stole from our government treasury amounting
        to US$55 Billion Dollars (ref:ngrguardiannews.com) of July 2nd 1999. Even the London times of July 1998 reported that General Abacha has over US$3.Billion dollars in one account overseas. We decided to conceal this one (1)box till the situation is calm and quite on the issue. The box was thus deposited with a security company here in Nigeria and tagged as "Precious Stones and Jewellry" in other that its
        content will not be discovered. Now that all is calm, we (myself and two of my colleagues in the operations team) are now ready to move this box out of the country through a diplomatic arrangement which is the safest means. 

        However as government officials the Civil Service Code of Conduct does not allow us by law to operate any foreign account or own foreign investment and the amount of money that can be found in our account
        cannot be more than our salary on the average, thus our handicapp and our need for your assistance to help collect and keep safely in your account this money.

        Therefore we want you to assist us in moving this money out of Nigeria. We shall definitely compensate you handsomely for the assistance. We can do this by instructing the Security Company here in Nigeria to
        move the consignment to their affiliate branch office outside Nigeria through diplomatic means and the consignment will be termed as Precious Stones and Jewelleries" which you bought during your visit to Nigeria and is being transfered to your country from here for safe keeping. Then we can arrange to meet at the destination country to take the delivery of the consignment. You will thereafter open an account there and lodge the Money there and gradually instruct remittance to your Country. 

        This business is 100% risk free for you so please treat this matter with utmost confidentiality .If you indicate your interest to assist us please just e-mail me for more Explanation on how we plan to execute the transaction.

        Expecting your response urgently.

        Best regards,

        Mr. Ben Suleman

        Wed Oct 30 21:41:56 2002
        Return-Path: <james_ngola2002@maktoob.com>
        X-Sieve: cmu-sieve 2.0
        Return-Path: <james_ngola2002@maktoob.com>
        Message-Id: <200210310241.g9V2fNm6028281@cs.CU>
        From: "MR. JAMES NGOLA." <james_ngola2002@maktoob.com>
        Reply-To: james_ngola2002@maktoob.com
        To: webmaster@aclweb.org
        Date: Thu, 31 Oct 2002 02:38:20 +0000
        Subject: URGENT BUSINESS ASSISTANCE AND PARTNERSHIP
        X-Mailer: Microsoft Outlook Express 5.00.2919.6900 DM
        MIME-Version: 1.0
        Content-Type: text/plain; charset="us-ascii"
        Content-Transfer-Encoding: 8bit
        X-MIME-Autoconverted: from quoted-printable to 8bit by sideshowmel.si.UM id g9V2foW24311
        Status: O

        FROM:MR. JAMES NGOLA.
        CONFIDENTIAL TEL: 233-27-587908.
        E-MAIL: (james_ngola2002@maktoob.com).

        URGENT BUSINESS ASSISTANCE AND PARTNERSHIP.


        DEAR FRIEND,

        I AM ( DR.) JAMES NGOLA, THE PERSONAL ASSISTANCE TO THE LATE CONGOLESE (PRESIDENT LAURENT KABILA) WHO WAS ASSASSINATED BY HIS BODY GUARD ON 16TH JAN. 2001.


        THE INCIDENT OCCURRED IN OUR PRESENCE WHILE WE WERE HOLDING MEETING WITH HIS EXCELLENCY OVER THE FINANCIAL RETURNS FROM THE DIAMOND SALES IN THE AREAS CONTROLLED BY (D.R.C.) DEMOCRATIC REPUBLIC OF CONGO FORCES AND THEIR FOREIGN ALLIES ANGOLA AND ZIMBABWE, HAVING RECEIVED THE PREVIOUS DAY (USD$100M) ONE HUNDRED MILLION UNITED STATES DOLLARS, CASH IN THREE DIPLOMATIC BOXES ROUTED THROUGH ZIMBABWE.

        MY PURPOSE OF WRITING YOU THIS LETTER IS TO SOLICIT FOR YOUR ASSISTANCE AS TO BE A COVER TO THE FUND AND ALSO COLLABORATION IN MOVING THE SAID FUND INTO YOUR BANK ACCOUNT THE SUM OF (USD$25M) TWENTY FIVE MILLION UNITED STATES DOLLARS ONLY, WHICH I DEPOSITED WITH A SECURITY COMPANY IN GHANA, IN A DIPLOMATIC BOX AS GOLDS WORTH (USD$25M) TWENTY FIVE MILLION UNITED STATES DOLLARS ONLY FOR SAFE KEEPING IN A SECURITY VAULT FOR ANY FURTHER INVESTMENT PERHAPS IN YOUR COUNTRY. 

        YOU WERE INTRODUCED TO ME BY A RELIABLE FRIEND OF MINE WHO IS A TRAVELLER,AND ALSO A MEMBER OF CHAMBER OF COMMERCE AS A RELIABLE AND TRUSTWORTHY PERSON WHOM I CAN RELY ON AS FOREIGN PARTNER, EVEN THOUGH THE NATURE OF THE TRANSACTION WAS NOT REVEALED TO HIM FOR SECURITY REASONS.


        THE (USD$25M) WAS PART OF A PROCEEDS FROM DIAMOND TRADE MEANT FOR THE LATE PRESIDENT LAURENT KABILA WHICH WAS DELIVERED THROUGH ZIMBABWE IN DIPLOMATIC BOXES. THE BOXES WERE KEPT UNDER MY CUSTODY BEFORE THE SAD EVENT THAT TOOK THE LIFE OF (MR. PRESIDENT).THE CONFUSION THAT ENSUED AFTER THE ASSASSINATION AND THE SPORADIC SHOOTING AMONG THE FACTIONS, I HAVE TO RUN AWAY FROM THE COUNTRY FOR MY DEAR LIFE AS I AM NOT A SOLDIER BUT A CIVIL SERVANT I CROSSED RIVER CONGO TO OTHER SIDE OF CONGO LIBREVILLE FROM THERE I MOVED TO THE THIRD COUNTRY GHANA WHERE I AM PRESENTLY TAKING REFUGE. 

        AS A MATTER OF FACT, WHAT I URGENTLY NEEDED FROM YOU IS YOUR ASSISTANCE IN MOVING THIS MONEY INTO YOUR ACCOUNT IN YOUR COUNTRY FOR INVESTMENT WITHOUT RAISING EYEBROW. FOR YOUR ASSISTANCE I WILL GIVE YOU 20% OF THE TOTAL SUM AS YOUR OWN SHARE WHEN THE MONEY GETS TO YOUR ACCOUNT, WHILE 75% WILL BE FOR ME, OF WHICH WITH YOUR KIND ADVICE I HOPE TO INVEST IN PROFITABLE VENTURE IN YOUR COUNTRY IN OTHER TO SETTLE DOWN FOR MEANINGFUL LIFE, AS I AM TIRED OF LIVING IN A WAR ENVIRONMENT. 

        THE REMAINING 5% WILL BE USED TO OFFSET ANY COST INCURRED IN THE CAUSE OF MOVING THE MONEY TO YOUR ACCOUNT. IF THE PROPOSAL IS ACCEPTABLE TO YOU PLEASE CONTACT ME IMMEDIATELY THROUGH THE ABOVE TELEPHONE AND E-MAIL, TO ENABLE ME ARRANGE FACE TO FACE MEETING WITH YOU IN GHANA FOR THE CLEARANCE OF THE FUNDS BEFORE TRANSFRING IT TO YOUR BANK ACCOUNT AS SEEING IS BELIEVING. 

        FINALLY, IT IS IMPORTANT ALSO THAT I LET YOU UNDERSTAND THAT THERE IS NO RISK INVOLVED WHATSOEVER AS THE MONEY HAD NO RECORD IN KINSHASA FOR IT WAS MEANT FOR THE PERSONAL USE OF (MR. PRESIDEND ) BEFORE THE NEFARIOUS INCIDENT OCCURRED, AND ALSO I HAVE ALL THE NECESSARY DOCUMENTS AS REGARDS TO THE FUNDS INCLUDING THE (CERTIFICATE OF DEPOSIT), AS I AM THE DEPOSITOR OF THE CONSIGNMENT.


        LOOKING FORWARD TO YOUR URGENT RESPONSE.

        YOUR SINCERELY,

        MR. JAMES NGOLA. """)