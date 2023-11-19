from math import gcd
from functools import reduce

def find_gcd(distances):
    # En büyük ortak böleni hesapla
    x_gcd = reduce(gcd, distances)
    return x_gcd

def repeated_trigrams_sorted_with_gcd(text, min_frequency=2):
    trigram_positions = {}

    # Adım 1: Trigramları Bulma
    for i in range(len(text) - 2):
        trigram = text[i:i + 3]
        if trigram in trigram_positions:
            trigram_positions[trigram].append(i)
        else:
            trigram_positions[trigram] = [i]

    # Adım 2: Tekrar Eden Trigramları ve Frekansları ile Uzaklıklarını Yazdırma
    repeated_trigrams = {trigram: positions for trigram, positions in trigram_positions.items() if len(positions) > 1}
    
    # Frekansları ve uzaklıkları kullanarak tekrar eden trigramları sırala
    sorted_trigrams = sorted(repeated_trigrams.items(), key=lambda x: (len(x[1]), x[1]), reverse=True)
    
    print(f"Sorted Repeated Trigrams with Frequencies, Distances, and GCDs (Frequency > {min_frequency}):")
    for trigram, positions in sorted_trigrams:
        frequency = len(positions)
        if frequency > min_frequency:
            distances = [positions[i + 1] - positions[i] for i in range(len(positions) - 1)]
            gcd_value = find_gcd(distances)
            print(f"Trigram: {trigram}, Frequency: {frequency}, Distances: {distances}, GCD: {gcd_value}")

# Şifreli metni tanımla
cipher_text = "zngpımnpgnegşccvcyczvçosnföojepivfbbnşunküoznşarnrojoinbeojekgşccvcyczvçoonrhtgapüfteasşyıjnpeıjşşüapöbgşfivröşşrynkidrüşşrcrfnvccvvcaığmojpçporpsynghsivrymsvfevpolngğihkjnacryifenpnaeıjşküüunpeıleoirvuaühçcghpovküsuğiunğiscöşşvrösmifneufuühhftılşaenscfkzccsrujzöücvaliığkoeeşzvrzniveejsdeeşşveneeiyığşzoıgzıüüğoopneçiengufgpscfjebşülnjjuebgmicpezrrüsugmpnybeeğlfzmğjoejçilbscdidnfüighçcisnfnğüöizarskşdüpvçfanieifıfjoejççföejğisnfşzcrezşmpscnghsltdnpşığssenercddrüsenşmönciımuigfçükcvshfirorighççrüüçhilnleoinfvijnsvftpsysrömiıbübseeeznrcygnplıhüfgejizlmjvfoııpvüzçvfezpiübvcyndafüfgejipjeğidccvmiopvepmünvrrücşrünljoipçpocğçyıüfçükcvshfirorighççrckçirrscyıröocijıfmcpıpmisnfşsjıfhfömğüfiçsbsrööngmefişueeşfdeünscöznrcygnrüüvhugcvcsüöşarnroyıckvcugıgüorrskngmmnzdnfnafıeeiunjyolıfşpengnemsönvfıeğisnfşsubğhfjmğmfjtrçfanşştersucpıjnodngiıuıünpbvskfhdverüsvjoeıtnpğpsymühvorüüvfrrygiprhcyfstfgsnroıgcpzşyrçscgcpçvrüüçyoglvviglvcpğsnçböpshfdmğmfgnföoeığvidzvmoipççfgvvpolngşscdünpchçpiifçcmühvoıüjçcokngkognmnrcöfşgcpzşyrçscsnlvyıcvfnvcçveokzçcsüömşvsasvftpsmiivggjiıüiabsüikcüçdofgçüodnlüilrvhugımşscçıyilngzvyeğşervpzşcybfpmönnpğshvooıçdilnaşkcfççtjçsüıüüküiifnübgrsuarhccgmzvviepvcoeışarnrünşfırfşğpsygcpzşyrçscsnlvyıcvfnvcnlivrrsudüüçyidığmocyfnvcsçubieşşrügvufezpiübçsçfanizrfeeefumjüfiıaşacrıpvüzçvıüöçriuıyşscdpirgmrkfcyscföeğmiznfidgmrisrsüioköncfsnfnşsnföojepivfbbnşunkşdüzçdacügnpkıeüoghvçrğjsyrrygszlmjivyıöndüsçüodnğzçrvpzşdbfecibğgşlıeyteşdşjcügirrücyırcvutsnefvmpndrrücyırçvcrüygnycnuşşcpeizrrsyngbğşçüükşaüşfvfjmynrjıynycçfnarvscrrssyrcvsyyfbyciuemssbdksşbiıpvüstşrüüçyogfçeoirveippvcognüzliaüişjeğidcfsufgpcpnlıeytynjşzcrönanfçefdfçciövvükcüçdofgçüodujzöüzvurcifnvcfçlofnğmirpscfdçnufimüipclvmivpvciötğnrcöpgvnzoüsüömnıcüpgpjıeüojeğçiznmşscsünmühvoofnrivyıöndüsçüodzvaşuıjzrrsscfkzccsrgcğirpsynghsfefeğnrürsyrrüüzplşjiüişzcffmgseuebnıüiçvopnknıcssvodefişbsüigcpçvyüpönaüöğzrğoçuküpçdsüpvcoötğüighçcisnfnşyıfnğükvzıröfişfmljoengiırrfivbçveokzçcsüömşvyışıilıeyodbğşçüükşaüvçöanfçükcvshfirorighççrckçjuebggpbvsöitrçdogıeivkmğöignlşsdeğüfimşşrcrknrvesüoöımüiinşizrücüfimgnemsfivbçfihrkchfdefidrsöntgepaşoıjvirhcyfmrneçrhvmigfçcgcpzşyrçscsnlvyıcvfşlcfıücfbbircsvöierçdacüşadeışşvstfgsnsmgvdnpnğmrbfvcçveogıkileepiğrkcivlmünlüüfnvrümivröünçrrvmişıeeoi"

# Tekrar eden trigramları, frekansları, uzaklıkları ve GCD'leri sıralı şekilde yazdır (Frekansı 2'den büyük olanlar)
repeated_trigrams_sorted_with_gcd(cipher_text, min_frequency=2)
