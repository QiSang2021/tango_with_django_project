import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page # import project setting

def populate():
    # create lists of dictionaries containing pages that add to each category
    A_pages = [
        {
         'clothname': 'Ovresized shirt in acid wash denim', 
         'description': 'Boxy oversized solid denim button-down shirt in seasonal acid wash.',
         'url': 'https://www.alexanderwang.com/gb-en/OVERSIZED-SHIRT-IN-ACID-WASH-DENIM-UDC3212993323/',
         'views': 8,
         'price': 425.00,
         'typeAuto':1},
        {
         'clothname': 'Stovepipe jean in pebble bleach denim', 
         'description': 'high-waisted stretch denim stovepipe jeans in pebble bleach indigo wash with a dipped back waistband.',
         'url': 'https://www.alexanderwang.com/gb-en/STOVEPIPE-JEAN-IN-PEBBLE-BLEACH-DENIM+4DC2204710270/',
         'views': 200,
         'price': 295.00,
         'typeAuto':1},
        {
         'clothname': 'Long-sleeve tee in acid wash jersey', 
         'description': 'long- sleeve acid wash high twist jersey tee with repeating logo print at hem.',
         'url': 'https://www.alexanderwang.com/gb-en/LONG-SLEEVE-TEE-IN-ACID-WASH-JERSEY+UCC3211012007/',
         'views': 30,
         'price': 190.00,
         'typeAuto':1} ]

    B_pages = [
        {
         'clothname': 'Mid-length chelsea heritage trench coat', 
         'description':'The neatly tailored Chelsea Trench coat s cut by the brand iconic Gabadian craftsman, with narrow shoulders, waist design and Vintage check lining, showing the inspirational style of the collection.',
         'url': 'https://uk.burberry.com/the-mid-length-chelsea-heritage-trench-coat-p40733761/',
         'views': 340,
         'price': 1650.00,
         'typeAuto':1},
        {
         'clothname': 'Epaulette detail silk crepe de chine shirt', 
         'description':'Italian worsted silk crepe shirt with supple textture. Incorporating a small stand-up collar and epaulettes design, inspired by the trench coat.',
         'url': 'https://uk.burberry.com/epaulette-detail-silk-crepe-de-chine-shirt-p80433431/',
         'views': 15,
         'price': 790.00,
         'typeAuto':1},
        {
         'clothname': 'Check wool cashmere jacquard cardigan', 
         'description':'The cardigan is made of selected wool and cashmere blended fabrics, presenting a jacquard worsted check pattern, with a rough ribbed trim design.',
         'url': 'https://uk.burberry.com/check-wool-cashmere-jacquard-cardigan-p80412841/',
         'views': 63,
         'price': 690.00,
         'typeAuto':1} ]

    C_pages = [
        {
         'clothname': 'Wool tweed light pink, sliver & black jacket', 
         'description':'',
         'url': 'https://www.chanel.com/gb/fashion/p/P71173V62512ND316/jacket-wool-tweed/',
         'views': 988,
         'price': 5430.00,
         'typeAuto':1},
        {
         'clothname': 'Cotton lignt pick, black, ecru & silver trousers', 
         'description':'',
         'url': 'https://www.chanel.com/gb/fashion/p/P71172V62780NE383/trousers-cotton/',
         'views': 300,
         'price': 3200.00,
         'typeAuto':1},
        {
         'clothname': 'Cotton lace black & silver dress', 
         'description':'',
         'url': 'https://www.chanel.com/gb/fashion/p/P71184V6283994305/dress-cotton-lace/',
         'views': 36,
         'price': 7690.00,
         'typeAuto':1} ]

    D_pages = [
        {
         'clothname': 'Sailor collar cardigan', 
         'description':'Crafted in ecru wool and cashmere knit, it is distinguished by a sailor collar, further embellished with brand signature. The creation is completed by navy blue contrasting details and signature buttons, enhanced by an anchor. The warm and comfortable cardigan can be worn with any outfit year-round.',
         'url': 'https://www.dior.com/en_gb/products/couture-154G02AM305_X5801-sailor-collar-cardigan-ecru-wool-and-cashmere-knit/',
         'views': 420,
         'price': 1800.00,
         'typeAuto':1},
        {
         'clothname': 'Dior amour hooded short anorak', 
         'description':'The hooded short anorak, part of the Dioramour capsule, boasts the black, white and red D-Chess Heart motif. Crafted in technical taffeta jacquard, the design features a zipped neckline, a piped pocket, two side pockets and a flap adorned with the brand signature. Its relaxed silhouette will complement any casual look this season and it can be coordinated with other Dioramour creations to complete the look.',
         'url': 'https://www.dior.com/en_gb/products/couture-157C09A2732_X0835-dioramour-hooded-short-anorak-black-white-and-red-d-chess-heart-technical-taffeta-jacquard/',
         'views': 610,
         'price': 2800.00,
         'typeAuto':1},
        {
         'clothname': 'Dior and Kenny Scharf jacket', 
         'description':'The jacket is part of the collaboration with the artist Kenny Scharf. Crafted in blue silk jacquard, the design features an all-over tonal DIOR AND KENNY SCHARF motif with a satin effect. The style, with its classic silhouette, can be coordinated with the matching pants to complete the look.',
         'url': 'https://www.dior.com/en_gb/products/couture-193C251A5250_C585-dior-and-kenny-scharf-jacket-blue-silk-jacquard/',
         'views': 98,
         'price': 2400.00,
         'typeAuto':1} ]

    F_pages = [
        {
         'clothname': 'Brown satin dress', 
         'description':'Slip dress with thin shoulder straps and soft skirt with asymmetric hem. Made of shiny satin in taupe, decorated with FF Karligraphy openwork embroidery.',
         'url': 'https://www.fendi.com/gb/woman/ready-to-wear/p-fdb667agucf1eps/',
         'views': 12,
         'price': 3300.00,
         'typeAuto':1},
        {
         'clothname': 'Black milk coat', 
         'description':'Midi coat with collar and zip fastening. Leather belt with metal FF buckle. Made of black mink. Decorated with a Pequin diagonal motif and contrasting elaphe inserts.',
         'url': 'https://www.fendi.com/gb/woman/ready-to-wear/p-fnf93lahouf0gme/',
         'views': 53,
         'price': 23500.00,
         'typeAuto':1},
        {
         'clothname': 'Black piqué sweatshirt', 
         'description':'Regular fit, long-sleeved, crew-neck sweatshirt. Ribbed collar, cuffs and edges. Made with black cotton piqué. Decorated with tone on tone flocked FF motif printed all over.',
         'url': 'https://www.fendi.com/gb/ready-to-wear-man/sweatshirt-fy1077afrjf0abb/',
         'views': 5,
         'price': 850.00,
         'typeAuto':1},
         {
         'clothname': 'Brown silk shirt', 
         'description':'Oversized shirt with Italian-style collar and short sleeves. Concealed button fastening. Made of silk with a brown all-over FF Vertigo motif print. Trimmed with trekking style cord on the collar and front fastening.',
         'url': 'https://www.fendi.com/gb/ready-to-wear-man/shirt-fs0795ag9df1440/',
         'views': 90,
         'price': 895.00,
         'typeAuto':1} ]

    G_pages = [
        {
         'clothname': 'Square G check tweed jacket', 
         'description':'The Ouverture collections plays with emblematic motifs and materials, mixing them with House codes to create something new. This tweed jacket pairs a check motif with Guccio monogram, while blue and red trims are a nod to the emblematic Web.',
         'url': 'https://www.gucci.com/uk/en_gb/pr/women/ready-to-wear-for-women/jackets-for-women/blazers-for-women/square-g-check-tweed-jacket-p-652255ZAGLP2254/',
         'views': 29,
         'price': 2050.00,
         'typeAuto':1},
        {
         'clothname': 'Floral wool and cotton knit', 
         'description':'Flowers and embroideries define the knitwear of the Ouverture collection. Presented in a variety of colours, they are reminiscent of handmade pieces from the vintage world. Here, an embroidered floral motif elevates this off-white jumper.',
         'url': 'https://www.gucci.com/uk/en_gb/pr/women/ready-to-wear-for-women/jumpers-and-cardigans-for-women/jumpers-for-women/floral-wool-and-cotton-knit-p-653328XKBS99783/',
         'views': 460,
         'price': 1250.00,
         'typeAuto':1},
        {
         'clothname': 'Disney x Gucci oversize T-shirt', 
         'description':'The playful image of Mickey Mouse is displayed over the Gucci vintage logo and defines this white soft cotton T-shirt. In honour of the Chinese year of the Mouse, Disney’s legendary character appears throughout Gucci’s ready-to-wear and accessories for the Cruise 2020 collection, displayed as colourful prints, embroidered patches or jacquard motifs.',
         'url': 'https://www.gucci.com/uk/en_gb/pr/men/ready-to-wear-for-men/t-shirts-and-polo-shirts-for-men/t-shirts-for-men/disney-x-gucci-oversize-t-shirt-p-565806XJB669756/',
         'views': 5,
         'price': 400.00,
         'typeAuto':1} ]

    H_pages = [
        {
         'clothname': 'Brides de Gala belted tunic', 
         'description':'Belted tunic in "Brides de Gala en Desordre" printed silk twill (100% silk)',
         'url': 'https://www.hermes.com/uk/en/product/brides-de-gala-en-desordre-belted-tunic-H1H0609D92F38/',
         'views': 1,
         'price': 1550.00,
         'typeAuto':1},
        {
         'clothname': 'Brides de Gala long-sleeve sweater', 
         'description':'Long-sleeve sweater in Scottish cashmere with "Brides de Gala" intarsia motif (100% cashmere)',
         'url': 'https://www.hermes.com/uk/en/product/brides-de-gala-long-sleeve-sweater-H1H2606D20242/',
         'views': 28,
         'price': 1140.00,
         'typeAuto':1},
        {
         'clothname': 'Brides de Gala supple long-sleeve twillaine cardigan', 
         'description':'Supple long-sleeve twillaine cardigan in wool and cashmere tweed with "Brides de Gala" printed silk (68% wool, 29% cashmere, 3% polyamide)',
         'url': 'https://www.hermes.com/uk/en/product/brides-de-gala-supple-long-sleeve-twillaine-cardigan-H1H2802DG8I40/',
         'views': 57,
         'price': 2280.00
         ,'typeAuto':1} ]

    M_pages = [
        {
         'clothname': 'Cashmere and mohair cardigan', 
         'description':'Precious yarns and an ultra-feminine silhouette characterize this cashmere and mohair wool cardigan',
         'url': 'https://www.miumiu.com/gb/en/ready_to_wear/knitwear/products.cashmere_and_mohair_cardigan.MMF487_1Y4L_F0002.html/',
         'views': 63,
         'price': 1290.00,
         'typeAuto':1},
        {
         'clothname': 'Printed satin dress', 
         'description':'This satin minidress, characterized by a silhouette inspired by retro styles, has accents with romantic allure.',
         'url': 'https://www.miumiu.com/gb/en/ready_to_wear/dresses/products.printed_satin_dress.MF4360_1MP7_F0002.html/',
         'views': 282,
         'price': 1990.00,
         'typeAuto':1},
        {
         'clothname': 'Cady dress', 
         'description':'This cady evening dress comes alive with romantic allure expressed in the jeweled shoulder straps decorated with pearls that enhance the feminine line.',
         'url': 'https://www.miumiu.com/gb/en/ready_to_wear/dresses/products.cady_dress.MF4386_1ZEC_F0002.html/',
         'views': 557,
         'price': 1790.00,
         'typeAuto':1} ]

    P_pages = [
        {
         'clothname': 'Re-Nylon and jersey T-shirt', 
         'description':'This T-shirt is characterized by its contemporary streetwear allure and its oversized silhouette, emphasized by the sporty drawstring hem. A small pouch with an iconic triangular shape frames the enameled metal triangle logo. The garment combines jersey and Re-Nylon, a fabric made of regenerated nylon yarn.',
         'url': 'https://www.prada.com/gb/en/women/ready_to_wear/t-shirts_and_sweatshirts/products.re-nylon_and_jersey_t-shirt.135696_1XBH_F0002_S_212.html/',
         'views': 851,
         'price': 790.00,
         'typeAuto':1},
        {
         'clothname': 'Poplin dress', 
         'description':'An expression of lightness, this poplin dress reflects elegant yet ironic femininity. Layered ruffles decorate the full skirt and bodice characterized by a straight cut neckline supported by slim straps at the back that leave the back bare.',
         'url': 'https://www.prada.com/gb/en/women/ready_to_wear/dresses/products.poplin_dress.P3F25_1UCX_F0009_S_211.html/',
         'views': 52,
         'price': 2600.00,
         'typeAuto':1},
        {
         'clothname': 'Double Match poplin shirt', 
         'description':'Surf and Stripe, two of the most iconic prints of the brand, meet in the Double Match shirt made of stretch cotton and defined by its boxy cut that resembles bowling shirts. Part of Prada genetic code, recognizable and timeless prints have identified the collections of the brand since the 90s, creating bold combinations or emphasizing garments with traditional allure.',
         'url': 'https://www.prada.com/gb/en/men/ready_to_wear/shirts/products.double_match_poplin_shirt.UCS406_1ZSG_F0076_S_212.html/',
         'views': 79,
         'price': 850.00,
         'typeAuto':1} ]

    Y_pages = [
        {
         'clothname': 'Lace-up mini dress in wool jersey', 
         'description':'Long-sleeve mini dress featuring front welt pockets and a curved-omega chain lace-up front with a plunging v neckline.',
         'url': 'https://www.ysl.com/en-gb/dresses-and-skirts/lace-up-mini-dress-in-wool-jersey-657659Y288V1000.html/',
         'views': 467,
         'price': 1890.00,
         'typeAuto':1},
        {
         'clothname': 'Long belted jacket in wool jersey', 
         'description':'Long jacket with front buttons and a stand collar, featuring flap pockets and an adjustable, removable belt with contrasting buckle at the waist.',
         'url': 'https://www.ysl.com/en-gb/jackets/long-belted-jacket-in-wool-jersey-659808Y288V9601.html/',
         'views': 52,
         'price': 2175.00,
         'typeAuto':1},
        {
         'clothname': 'Tea blouse in silk satin', 
         'description':'long-sleeve tea blouse with a plunging v neckline and basque waist with covered buttons.',
         'url': 'https://www.ysl.com/en-gb/shirts-and-blouses/tea-blouse-in-silk-satin-646017Y001W9583.html/',
         'views': 43,
         'price': 1225.00,
         'typeAuto':1} ]

    # create a nested dictionary set categories
    # which is easier to iterate each data structure and add data to models
    cats = {'AlexanderWang': {'pages': A_pages},
            'Burberry': {'pages': B_pages},
            'Chanel': {'pages': C_pages},
            'Dior': {'pages': D_pages},
            'Fendi': {'pages': F_pages},
            'Gucci': {'pages': G_pages},
            'Hermes': {'pages': H_pages},
            'miumiu': {'pages': M_pages},
            'Prada': {'pages': P_pages},
            'YSL': {'pages': Y_pages} }

    # go through cats dictionary and add each category
    # add all associated pages for category
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['clothname'], p['description'], p['url'], p['views'], p['price'])

    # print out categories added
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, clothname, description, url, views=0, price=0):
    p = Page.objects.get_or_create(category=cat, clothname=clothname)[0]
    p.description=description
    p.url=url
    #p.img=img
    p.views=views
    p.price=price
    p.save()
    return p

def add_cat(brandname):
    c = Category.objects.get_or_create(brandname=brandname)[0]
    c.save()
    return c

# start execution
if __name__ == '__main__':
    print('Starting rango population script...')
    populate()