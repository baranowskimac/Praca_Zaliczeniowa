from OtoDomScrape import scrape_otodom_data

scrape_oto_dom = scrape_otodom_data(
    sprzedaz = 'sprzedaz', 
    apartament_type = 'mieszkanie', 
    region = 'mazowieckie',
    price_min = None,
    price_max = 150000,
    path_to_save_batch_files = 'bathfiles', 
    path_to_save_full_files = 'fullFile',
    sys_sleeping = 0.5
)