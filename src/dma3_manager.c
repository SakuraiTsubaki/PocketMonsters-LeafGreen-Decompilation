#include <stddef.h>
#include <stdint.h>

#define DMA3_REQUEST_COUNT 128

typedef uint8_t bool8;

struct Dma3Request
{
    const uint8_t *src;
    uint8_t *dest;
    uint16_t size;
    uint16_t mode;
    uint32_t value;
};

static struct Dma3Request gDma3Requests[DMA3_REQUEST_COUNT];
static volatile bool8 gDma3ManagerLocked;
static uint8_t gDma3RequestCursor;

void ClearDma3Requests(void)
{
    unsigned int i;

    gDma3ManagerLocked = 1;
    gDma3RequestCursor = 0;
    for (i = 0; i < DMA3_REQUEST_COUNT; i++)
    {
        struct Dma3Request *request = &gDma3Requests[i];
        request->size = 0;
        request->src = NULL;
        request->dest = NULL;
    }
    gDma3ManagerLocked = 0;
}
