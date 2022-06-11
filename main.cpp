#include <iostream>
#include <conio.h>
#include <ctime>
#include <fstream>
#include <string>

using namespace std;


time_t times = time(0);
tm *gottime = localtime(&times);
string year = to_string(1900+gottime->tm_year);
string month = to_string(1+gottime->tm_mon);
string day = to_string(gottime->tm_mday);
string Date = day+" "+month+" "+year;

bool isDateFound(string Date){
ifstream checker ("tracker.txt");
string x;
bool wasFound = false;
int line = 1;
if (checker.is_open())
{
    while (getline(checker,x)){
        if (x.find(Date) != string::npos){
            wasFound = true;}
                line++;
    }
    checker.close();
}
else
    cout<<"Couldnt open file";
return wasFound;
}

void printHistory(){
fstream moodTracker;
moodTracker.open("tracker.txt", ios::in);
if (moodTracker.is_open()){
    string read;
    while(getline(moodTracker, read)){
        cout<<read<<endl;
    }
    moodTracker.close();
}
}

int moodAsker(bool wasDateFound)
{
    if (wasDateFound==true){
    cout<<"Found input for mood rating for today. Printing your history instead."<<endl;
    printHistory();
    return 0;
} else{

cout<<"Hi, how did you feel today on a scale from 1 to 100? ";
int moodRating;
cin>>moodRating;

while (moodRating < 1 || moodRating >100){
cout<<"That was not a valid number. How did you feel today on a scale from 1 to 100? ";
cin>>moodRating;
}
return moodRating;
}
}

int moodTracking(bool isDateFound, string Date, int moodRating){
if (isDateFound==false){
fstream moodTracking;
moodTracking.open("tracker.txt", ios::app);
if (moodTracking.is_open()){
    moodTracking<<Date<<"; Mood - "<<moodRating<<"\n";
    moodTracking.close();
}
}
else return 0;

}

int main()
{
moodTracking(isDateFound(Date), Date, moodAsker(isDateFound(Date)));
}
