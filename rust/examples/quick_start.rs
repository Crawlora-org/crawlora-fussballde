use crawlora_fussballde::{
    Client, FussballdeClubSearchParams, ModelFussballdeClubSearchResponseDoc,
};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .fussballde
        .club_search(FussballdeClubSearchParams {
            text: Some("Bayern".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelFussballdeClubSearchResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
