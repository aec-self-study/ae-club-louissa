# Beschreibung des Modells: Customers

Das `customers`-Modell enthält die Stammdaten der Kunden des Coffee-Shops.

## Eingabedatenquellen
- **raw_customers**: Originaldaten der Kunden aus der Datenquelle.

## Transformationen
1. Bereinigung der Daten (z. B. Entfernen von Duplikaten).
2. Normalisierung von Namen und Adressen.
3. Hinzufügen von Berechnungen wie dem `customer_lifetime_value`.

## Ausgabe
Eine Tabelle mit den folgenden Spalten:
- `customer_id`: Eindeutige ID des Kunden.
- `first_name`: Vorname des Kunden.
- `last_name`: Nachname des Kunden.
- `email`: E-Mail-Adresse.
- `customer_lifetime_value`: Geschätzter Lebenszeitwert des Kunden.
