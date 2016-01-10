/* Test file for decomment50
 *
 * Trying to be as nasty as possible
 *
 */

int main(void)
{
    //comment woo
    int x = 8;
    
    // this is y
    char y = 'y'; // inline?
    for (int i = 0; /*break things?*/ i<3; i++)
    {
        // what
        int j = 5;//this?
    }
    
    // this is z
    // this another comment
    float z =/* break more things? */ 4.555;/***/
    
    char* = "// Not a real comment";
    char* = "/*also not a real comment */";
    char = '"'; // "what about this?"
}
