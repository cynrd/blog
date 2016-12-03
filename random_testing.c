//sources:
//* http://stackoverflow.com/questions/876605/multiple-child-process
//* http://stackoverflow.com/questions/440133/how-do-i-create-a-random-alpha-numeric-string-in-c
//* http://stackoverflow.com/questions/4182876/how-to-write-a-string-to-a-file-in-c
//* http://www.programmingsimplified.com/c-program-delete-file
//* https://www.codingunit.com/c-tutorial-searching-for-strings-in-a-text-file


#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define FORMAT_FILENAME "input_%d.txt"
#define FORMAT_FILENAME_OUT "output_%d.txt"
#define N 1


void gen_random(char *s, int len);
void deleteFiles(int i);
void deleteFile(char* filepath);
void save(const char * contents, int i);
int search(char *fname, char *str);

int main(int argc, char* argv[]) {
	pid_t pids[N];
	int i;
	int n = N;

	assert(argc == 2);

	srand(time(NULL)); 

	/* Start children. */
	for (i = 0; i < n; ++i) {
		if ((pids[i] = fork()) < 0) {
    		perror("fork");
    		abort();
  		} else if (pids[i] == 0) {
    		//DoWorkInChild();
			printf("in child %d\n", i);
			int length = rand() % 4096 + 1;
			char * str = malloc(length*sizeof(char));
			gen_random(str, length-1) ;
			printf("curr string: %s\n", str);
			save(str, i);
    		
			char filepath[80];
			sprintf(filepath, FORMAT_FILENAME, i);
			char filepathOut[80];
			sprintf(filepathOut, FORMAT_FILENAME_OUT, i);
			
			char cmd[1024];
			sprintf(cmd, "cat %s | while read -r line; do echo -e $line; done | valgrind --log-file=/dev/null %s 2>&1 > %s", filepath, argv[1], filepathOut);	
			printf("executing command: %s\n", cmd);
			int retValue = system(cmd);

			
			//int found = search(filepathOut, "Segmentation fault");
			if (retValue != 0) {
				printf("exit with some problem");
			} else {
				deleteFiles(i);
			}
			
			free(str);
    		exit(0);
  		}
	}

	/* Wait for children to exit. */
	int status;
	pid_t pid;
	while (n > 0) {
  		pid = wait(&status);
  		printf("Child with PID %ld exited with status 0x%x.\n", (long)pid, status);
  		--n;
	}
}


int search(char *fname, char *str) {
	FILE *fp;
	int line_num = 1;
	int find_result = 0;
	char temp[512];
	
	if((fp = fopen(fname, "r")) == NULL) {
		return(-1);
	}


	while(fgets(temp, 512, fp) != NULL) {
		if((strstr(temp, str)) != NULL) {
			printf("A match found on line: %d\n", line_num);
			printf("\n%s\n", temp);
			return 1;
			find_result++;
		}
		line_num++;
	}

	if(find_result == 0) {
		printf("\nSorry, couldn't find a match.\n");
	}
	
	//Close the file if still open.
	if(fp) {
		fclose(fp);
	}
   	return(0);
}

void deleteFiles(int i){
    char filepath[80];
	sprintf(filepath, FORMAT_FILENAME, i);
	deleteFile(filepath);
    char filepathOut[80];
	sprintf(filepathOut, FORMAT_FILENAME_OUT, i);
	deleteFile(filepathOut);
}
void deleteFile(char* filepath){
	int status = remove(filepath);
 
   if( status == 0 )
      printf("%s file deleted successfully.\n",filepath);
   else
   {
      printf("Unable to delete the file\n");
      perror("Error");
   }
}

void save(const char * contents, int i)
{
    char filepath[80];
	sprintf(filepath, FORMAT_FILENAME, i);
	FILE *fp = fopen(filepath, "ab");
    if (fp != NULL)
    {
        fputs(contents, fp);
        fclose(fp);
    }
}


void gen_random(char *s, int len) {
	static const char alphanum[] =
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
		" \n\t`~!@#$%^&*()-_=+[]\\{}|:\";',./<>?";
	int i;

    for (i = 0; i < len; ++i) {
        s[i] = alphanum[rand() % (sizeof(alphanum) - 1)];
    }

    s[len] = 0;
}

