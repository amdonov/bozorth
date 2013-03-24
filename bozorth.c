#include "bozorth.h"
#include <bozorth.h>

FILE *errorfp = FPNULL;
int verbose_main = 0;
int verbose_load = 0;
int verbose_bozorth = 0;
int m1_xyt = 0;
int max_minutiae = DEFAULT_BOZORTH_MINUTIAE;
int min_computable_minutiae = MIN_COMPUTABLE_BOZORTH_MINUTIAE;

intptr_t
load_template (char *minutiae_file)
{
  struct xyt_struct *templ;
  templ = bz_load (minutiae_file);
  return (intptr_t) templ;
}

int
compare_templates (intptr_t templ1, intptr_t templ2)
{
  return bozorth_main ((struct xyt_struct *) templ1,
		       (struct xyt_struct *) templ2);
}

void
free_template (intptr_t templ)
{
  free ((void *) templ);
}
