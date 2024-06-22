using Microsoft.EntityFrameworkCore;
using AuthService.Entities;

namespace AuthService.Data
{
    public class ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : DbContext(options)
    {
        public DbSet<Stock> Stocks { get; init; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Stock>().HasData(new List<Stock>
            {
                new Stock {Id = 1, Ticker = "AAPL", DateOfPrediction ="2024-17-06", PredictedReturn = 3.34, DaysPredicted=30},
                new Stock {Id = 2, Ticker= "NVDA", DateOfPrediction="2024-17-06", PredictedReturn = -0.21, DaysPredicted=30}
            });

            base.OnModelCreating(modelBuilder);
        }
    }
}
