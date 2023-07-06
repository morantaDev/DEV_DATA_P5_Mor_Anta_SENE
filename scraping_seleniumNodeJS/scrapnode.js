const {Builder, By, until}=require("selenium-webdriver")

async function runScript(){
    const driver = await new Builder().forBrowser('chrome').build();


    try{
        await driver.get("https://www.farmmachinerysales.com.au/items/tillage-seeding-category/?offset=0");

        await driver.wait(until.elementsLocated(By.css('.key-details__value')), 5000);

        const values = await driver.findElements(By.className('key-details__value'));

        for(const val of values){
            const value = await val.getText();
            console.log(value);
        }

    } catch (error) {
        console.error("An error occurred:", error);
    }finally {
        await driver.quit();
    }
}
runScript()