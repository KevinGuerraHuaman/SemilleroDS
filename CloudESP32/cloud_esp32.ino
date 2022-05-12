#include <WiFi.h>
const char* ssid = "****"; 
const char* pass = "****"; 
WiFiClient client;


#include "ThingSpeak.h"
unsigned long Channel_ID = 1716252;
const char * WriteAPIKey = "BDZ2PFWVVMS3QNIJ"; 

#include "model_tree_best.h"
Eloquent::ML::Port::DecisionTree clf;


void setup(){
  Serial.begin(115200); 
  Serial.println("Iniciando conexión Wifi");
  WiFi.begin(ssid, pass);
  
  //Minetras se conecta imprimirá ...
  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("Conexion establecida");
  ThingSpeak.begin(client); //Iniciar el servidor de ThingSpeak

  
}

void loop(){
  
  //float sensores[8] = {-0.15930679,  0.65959843, -0.66394571,  0.25970957, -0.41468499, 0.24651935,  0.3766817 , -0.76024259};
  
  ThingSpeak.setField(1, dataset[conta]); 
  //Transmitir los datos al sevidor ThingSpeak
  int estado = ThingSpeak.writeFields(Channel_ID, WriteAPIKey);

  if (estado==200){
    Serial.println("Se envió");
  }
  else{
    Serial.println("problemas para enviar "+String(estado));
  }

  delay(5000);
  delay(5000);
}
