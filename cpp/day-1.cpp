    
    // Declare second integer, double, and String variables.
    int i2;
    double d2;
    string s2 = "";

    // Read and save an integer, double, and String to your variables.
    scanf("%d", &i2); 
    scanf("%lf", &d2);
    if (getline(cin >> ws, s2)) { // eat whitespace
        getline(cin, s2);
    }
    
    // Print the sum of both integer variables on a new line.
    printf("%d\n", i+i2);

    // Print the sum of the double variables on a new line.
    printf("%.1lf\n", d+d2);

    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    printf("%s%s", s.c_str(), s2.c_str());    
