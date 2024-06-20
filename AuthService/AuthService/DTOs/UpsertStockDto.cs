namespace AuthService.DTOs
{
    public class UpsertStockDto
    {
        public string Ticker { get; init; } = "";
        public string DateOfPrediction { get; init; } = "";
        public double PredictedReturn { get; init; }
        public int DaysPredicted { get; init; }
    }
}
