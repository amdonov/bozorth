#include <stdint.h>

intptr_t load_template (char *minutiae_file);
void free_template (intptr_t templ);
int compare_templates (intptr_t templ1, intptr_t templ2);
