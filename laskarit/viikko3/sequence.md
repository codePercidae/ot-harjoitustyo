```Mermaid
    sequenceDiagram
    	Main->>+Car: Machine()
   	 Car->>Tank: FuelTank()
   	 Car->>Tank: fill(40)
   	 Car->>Motor: Engine(Tank)
   	 Motor->>Tank: fuel_tank()
   	 Car-->>Main: 
   	 Main->>+Car: drive()
   	 Car->>+Motor: start()
   	 Motor->>Tank: consume(5)
   	 Motor-->>-Car: 
   	 Car->>+Motor: is_running()
   	 Motor->>Tank: fuel_contents()
   	 Tank-->>Motor: 40
   	 Motor-->>-Car: True
   	 Car->>+Motor: use_energy()
   	 Motor->>-Tank: consume(10)
   	 Car-->>Main: 
```    
