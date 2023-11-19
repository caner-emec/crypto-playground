# Şifreli metni tanımla
cipher_text = "zngpımnpgnegşccvcyczvçosnföojepivfbbnşunküoznşarnrojoinbeojekgşccvcyczvçoonrhtgapüfteasşyıjnpeıjşşüapöbgşfivröşşrynkidrüşşrcrfnvccvvcaığmojpçporpsynghsivrymsvfevpolngğihkjnacryifenpnaeıjşküüunpeıleoirvuaühçcghpovküsuğiunğiscöşşvrösmifneufuühhftılşaenscfkzccsrujzöücvaliığkoeeşzvrzniveejsdeeşşveneeiyığşzoıgzıüüğoopneçiengufgpscfjebşülnjjuebgmicpezrrüsugmpnybeeğlfzmğjoejçilbscdidnfüighçcisnfnğüöizarskşdüpvçfanieifıfjoejççföejğisnfşzcrezşmpscnghsltdnpşığssenercddrüsenşmönciımuigfçükcvshfirorighççrüüçhilnleoinfvijnsvftpsysrömiıbübseeeznrcygnplıhüfgejizlmjvfoııpvüzçvfezpiübvcyndafüfgejipjeğidccvmiopvepmünvrrücşrünljoipçpocğçyıüfçükcvshfirorighççrckçirrscyıröocijıfmcpıpmisnfşsjıfhfömğüfiçsbsrööngmefişueeşfdeünscöznrcygnrüüvhugcvcsüöşarnroyıckvcugıgüorrskngmmnzdnfnafıeeiunjyolıfşpengnemsönvfıeğisnfşsubğhfjmğmfjtrçfanşştersucpıjnodngiıuıünpbvskfhdverüsvjoeıtnpğpsymühvorüüvfrrygiprhcyfstfgsnroıgcpzşyrçscgcpçvrüüçyoglvviglvcpğsnçböpshfdmğmfgnföoeığvidzvmoipççfgvvpolngşscdünpchçpiifçcmühvoıüjçcokngkognmnrcöfşgcpzşyrçscsnlvyıcvfnvcçveokzçcsüömşvsasvftpsmiivggjiıüiabsüikcüçdofgçüodnlüilrvhugımşscçıyilngzvyeğşervpzşcybfpmönnpğshvooıçdilnaşkcfççtjçsüıüüküiifnübgrsuarhccgmzvviepvcoeışarnrünşfırfşğpsygcpzşyrçscsnlvyıcvfnvcnlivrrsudüüçyidığmocyfnvcsçubieşşrügvufezpiübçsçfanizrfeeefumjüfiıaşacrıpvüzçvıüöçriuıyşscdpirgmrkfcyscföeğmiznfidgmrisrsüioköncfsnfnşsnföojepivfbbnşunkşdüzçdacügnpkıeüoghvçrğjsyrrygszlmjivyıöndüsçüodnğzçrvpzşdbfecibğgşlıeyteşdşjcügirrücyırcvutsnefvmpndrrücyırçvcrüygnycnuşşcpeizrrsyngbğşçüükşaüşfvfjmynrjıynycçfnarvscrrssyrcvsyyfbyciuemssbdksşbiıpvüstşrüüçyogfçeoirveippvcognüzliaüişjeğidcfsufgpcpnlıeytynjşzcrönanfçefdfçciövvükcüçdofgçüodujzöüzvurcifnvcfçlofnğmirpscfdçnufimüipclvmivpvciötğnrcöpgvnzoüsüömnıcüpgpjıeüojeğçiznmşscsünmühvoofnrivyıöndüsçüodzvaşuıjzrrsscfkzccsrgcğirpsynghsfefeğnrürsyrrüüzplşjiüişzcffmgseuebnıüiçvopnknıcssvodefişbsüigcpçvyüpönaüöğzrğoçuküpçdsüpvcoötğüighçcisnfnşyıfnğükvzıröfişfmljoengiırrfivbçveokzçcsüömşvyışıilıeyodbğşçüükşaüvçöanfçükcvshfirorighççrckçjuebggpbvsöitrçdogıeivkmğöignlşsdeğüfimşşrcrknrvesüoöımüiinşizrücüfimgnemsfivbçfihrkchfdefidrsöntgepaşoıjvirhcyfmrneçrhvmigfçcgcpzşyrçscsnlvyıcvfşlcfıücfbbircsvöierçdacüşadeışşvstfgsnsmgvdnpnğmrbfvcçveogıkileepiğrkcivlmünlüüfnvrümivröünçrrvmişıeeoia"

# Sütun sayısı 5 olan 2 boyutlu array
sutun_sayisi = 5
array_2d = [list(cipher_text[i:i+sutun_sayisi]) for i in range(0, len(cipher_text), sutun_sayisi)]

# Her bir sütun için frekans analizi yap
for i in range(min(len(array_2d[0]), len(array_2d[1]), len(array_2d[2]), len(array_2d[3]), len(array_2d[4]))):
    column = [row[i] for row in array_2d]
    frekans = {char: column.count(char) for char in set(column)}
    toplam_karakter_sayisi = len(column)
    
    # Frekansa göre büyükten küçüğe sırala
    sorted_frekans = sorted(frekans.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\nFrekans Analizi - Sütun {i + 1}:\n")
    print("{:<5} {:<5} {:<10}".format("Char", "Count", "Percentage"))
    print("-" * 30)
    
    for char, count in sorted_frekans:
        yuzde = (count / toplam_karakter_sayisi) * 100
        print("{:<5} {:<5} {:<10.2f}%".format(char, count, yuzde))
