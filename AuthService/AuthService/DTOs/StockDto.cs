namespace AuthService.DTOs
{
    public class StockDto
    {

        public int Id { get; init; }
        public string Ticker { get; init; } = "";
        public string DateOfPrediction { get; init; } = ""; 
        public float PredictedReturn { get; init; }
        public int DaysPredicted { get; init; } 
    }
}
