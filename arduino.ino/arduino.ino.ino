int segmentos[] = {2, 3, 4, 5, 6, 7, 8};

byte numeros[6][7] = {
  {0, 0, 0, 0, 0, 0, 1},  // 0
  {1, 0, 0, 1, 1, 1, 1},  // 1
  {0, 0, 1, 0, 0, 1, 0},  // 2
  {0, 0, 0, 0, 1, 1, 0},  // 3
  {1, 0, 0, 1, 1, 0, 0},  // 4
  {0, 1, 0, 0, 1, 0, 0}   // 5
};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 7; i++) {
    pinMode(segmentos[i], OUTPUT);
    digitalWrite(segmentos[i], HIGH);  
  }
}

void loop() {
  if (Serial.available() > 0) {
    int numero = Serial.read() - '0';

    if (numero >= 0 && numero <= 5) {
      mostrarNumero(numero);
    }
  }
}

void mostrarNumero(int n) {
  for (int i = 0; i < 7; i++) {
    digitalWrite(segmentos[i], numeros[n][i]);
  }
}


