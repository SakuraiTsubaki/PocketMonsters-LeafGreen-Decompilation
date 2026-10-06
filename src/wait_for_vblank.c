#include <stdint.h>

struct MainVBlankState
{
    uint8_t unknown_000[0x1C];
    volatile uint16_t intrCheck;
};

extern struct MainVBlankState gMain;

enum { INTR_FLAG_VBLANK = 1 };

/* BPGJ-rev0: 0x08000890..0x080008b8. */
void WaitForVBlank(void)
{
    gMain.intrCheck &= (uint16_t)~INTR_FLAG_VBLANK;
    while (!(gMain.intrCheck & INTR_FLAG_VBLANK))
    {
    }
}

