#include <iostream>
#include <cstdlib>
#include <chrono>
#include <windows.h>

using namespace std;

int main(){
  string Char;
  string act;
  string a = "Move";
  string b = "Check Inventory";
  string c = "Quit";
  int H = 100;
  int dice = 10;
  int store;
  int num = 3;
  string inv[store];
  string nar[num] = {"0", "You see food in the distance.", "You see an enemy in the distance."};
  
  cout << "Enter your name: ";
  cin >> Char;
  cout << "Welcome, " << Char << "!" << endl;

  while(H > 0){
    cout << "\n" << "Actions:";
    cout << "\n" << a << "\n" << b << "\n" << c << endl;
    cout << "\nEnter the action you want to do: ";
    cin >> act;
    if (act == c) {
      break;
    } else if (act == a) {
      cout << "You moved " << 1 + rand() % dice << " tiles." << endl;
      Sleep(5);
      cout << "..." << endl;
      Sleep(5);
      cout << "..." << endl;
      Sleep(5);
      cout << nar[1 + rand() % 2] << endl;
      if (dice == num) {
        cout << "Choices: " << endl;
      }
    } else if (act == b) {
      for (int i = 0; i < store; i++)
        cout << inv[i] << endl;
    } else
      continue;
  }
}
