# novel = "Wuthering Heights" 

def bronte(novel):
    
    charlotte = ["The Professor", "Jane Eyre", "Shirley", "Villette"] 
    emily = ["Wuthering Heights"] 
    anne = ["Agnes Grey", "The Tenant of Wildfell Hall"] 
    
    bronte_checks = {"charlotte": 0, "emily": 0, "anne" : 0} 
    
    if novel in charlotte: 
        bronte_checks["charlotte"] = bronte_checks["charlotte"] + 1
        print("Charlotte Brontë wrote", novel) 
    elif novel in emily: 
        bronte_checks["emily"] = bronte_checks["emily"] + 1
        print("Emily Brontë wrote", novel)
    elif novel in anne: 
        bronte_checks["anne"] = bronte_checks["anne"] + 1
        print("Anne Brontë wrote", novel) 
    else: print(novel, "was not written by one of the Brontë sisters")


    print(bronte_checks)
