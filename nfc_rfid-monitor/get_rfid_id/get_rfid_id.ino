// modified this example to just get the id of the card
//This example reads all MIFARE memory block from 0x00 to 0x63. It is tested with a new MIFARE 1K cards. Uses default keys for authentication.
//Contributed by Seeed Technology Inc (www.seeedstudio.com)

#include <PN532.h>

#define SCK 13
#define MOSI 11
#define SS 10
#define MISO 12

PN532 nfc(SCK, MISO, MOSI, SS);

void setup(void) {
    Serial.begin(9600);

    nfc.begin();

    uint32_t versiondata = nfc.getFirmwareVersion();
    if (! versiondata) {
        while (1); // halt
    }

    // configure board to read RFID tags and cards
    nfc.SAMConfig();
}


void loop(void) {
    uint32_t id;
    // look for MiFare type cards
    id = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A);

 
    if (id != 0)
    {
      Serial.println(id);
    }
    delay(200);
}

