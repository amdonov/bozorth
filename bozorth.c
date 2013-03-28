#include "bozorth.h"
#include <bozorth.h>
#include <string.h>

FILE *errorfp = FPNULL;
int verbose_main = 0;
int verbose_load = 0;
int verbose_bozorth = 0;
int m1_xyt = 0;
int max_minutiae = DEFAULT_BOZORTH_MINUTIAE;
int min_computable_minutiae = MIN_COMPUTABLE_BOZORTH_MINUTIAE;

void
load_template (char *minutiae_file, signed char buffer[2404])
{
  struct xyt_struct *templ;
  templ = bz_load (minutiae_file);
  memcpy(buffer,templ,2404); 
  free(templ);
}

int
compare_templates (signed char templ1[2404], signed char templ2[2404])
{
  return bozorth_main ((struct xyt_struct *) templ1,
		       (struct xyt_struct *) templ2);
}
