#Class - practice task
#class definition
class laptop():
    #init method for attributes -- similar to constructor in java
    def __init__(self,make,processor,RAM,storage,display):
        self.make = make
        self.processor = processor
        self.RAM = RAM
        self.storage = storage
        self.display = display

    #user defined functions    
    def laptop_dtl(self):
        BOLD = '\033[1m'
        END = '\033[0m'
        print(f"="*60)
        print(f"Following are the '{BOLD}{self.make}{END}' laptop specifications:\n")
        print(f"\t\u2022 {BOLD}Processor:{END} {self.processor}")
        print(f"\t\u2022 {BOLD}RAM:{END} {self.RAM}")
        print(f"\t\u2022 {BOLD}Storage:{END} {self.storage}")
        print(f"\t\u2022 {BOLD}Display:{END} {self.display} ")
    def ide(self,ide):
        BOLD = '\033[1m'
        END = '\033[0m'
        print(f"\t\u2022 {BOLD}IDEs installed{END} in the '{BOLD}{self.make}{END}' laptop are:")
        for i in ide:
            print(f"\t\t\u2022 {i}")
    def os(self):
        os_type = ""
        BOLD = '\033[1m'
        END = '\033[0m'
        if self.make.lower().startswith("mac"):
            os_type = "MacOS"
        elif self.make.lower().startswith("chrome"):
            os_type = "Chrome OS"
        elif self.make.lower().startswith("lenovo"):
            os_type = "Linux"
        else:
            os_type = "Microsoft Windows"           
        print(f"\t\u2022 {BOLD}OS installed{END} in '{BOLD}{self.make}{END}' laptop is: '{os_type}'")

#Object creation - instantiation
macbook_air = laptop("MacBook Air","Apple M4 chip","16 GB Unified memory","512 GB SSD Storage","13.6-inch Liquid Retina display with True Tone")
macbook_pro = laptop("MacBook Pro","Apple M5 chip","16 GB Unified memory","1 TB SSD Storage","14-inch Liquid Retina XDR display")
lenovo_thinkpad = laptop("Lenovo Thinkpad","AMD Ryzen™ 7 5825U","32 GB DDR4 memory","2 TB SSD Storage","16-inch")
chromebook = laptop("ChromeBook ","Intel Celeron","4 GB","64 GB eMMC storage","15.6 inch display")
hp_pavilion = laptop("HP Pavilion","Intel Core Processor (up to 4.1GHz)","16 GB","1TB SSD","15.6 inch")
hp_omnibook = laptop("HP OmniBook X","Intel Core Ultra 7","16 GB","1TB SSD","17.3 inch FHD Touchscreen")

#variable definition
ide_list = ["VS Code","JetBrains IDE","Eclipse"]
#Method calling
macbook_air.laptop_dtl()
macbook_air.os()
macbook_air.ide(ide_list)

macbook_pro.laptop_dtl()
macbook_pro.os()
macbook_pro.ide(ide_list)

lenovo_thinkpad.laptop_dtl()
lenovo_thinkpad.os()
lenovo_thinkpad.ide(ide_list)


chromebook.laptop_dtl()
chromebook.os()
chromebook.ide(ide_list)


hp_omnibook.laptop_dtl()
hp_omnibook.os()
hp_omnibook.ide(ide_list)


hp_pavilion.laptop_dtl()
hp_pavilion.os()
hp_pavilion.ide(ide_list)