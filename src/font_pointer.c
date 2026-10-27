struct FontInfo;

extern const struct FontInfo gFontInfos[];
extern const struct FontInfo *gFonts;

void SetFontsPointer(const struct FontInfo *fonts)
{
    gFonts = fonts;
}

void SetDefaultFontsPointer(void)
{
    SetFontsPointer(&gFontInfos[0]);
}
